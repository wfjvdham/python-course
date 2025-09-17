# Model Context Protocol (MCP)

Dit hoofdstuk legt uit wat het Model Context Protocol (MCP) is, waarom het bestaat en hoe je het kunt gebruiken om AI-modellen veilig en gestructureerd toegang te geven tot externe bronnen (zoals GitHub, databronnen of interne APIs).

## 1. Wat is MCP?
Het Model Context Protocol is een open protocol waarmee een AI model (client) op een consistente manier kan praten met "servers" die tooling, data of acties aanbieden. Het zorgt voor:
- Standaardisatie van interacties (resources, prompts, tools)
- Minder ad-hoc integratiecode per provider

Kort: MCP definieert een contract tussen een LLM-integratie (zoals een IDE of chat UI) en één of meerdere bronnen van data/acties.

## 2. Waarom MCP gebruiken?
| Voordeel | Uitleg |
|----------|-------|
| Scheiding van zorgen | Model blijft generiek; resource server regelt domeinlogica |
| Beveiliging | Alleen expliciet gedeclareerde tools/resources beschikbaar |
| Herbruikbaar | Zelfde server inzetbaar in meerdere clients |
| Observability | Gestandaardiseerde events/logging mogelijk |
| Extensibiliteit | Nieuwe resources toevoegen zonder client aanpassing |

## 3. Kernconcepten
| Concept | Beschrijving |
|---------|-------------|
| Client | De omgeving die het model host (bijv. Chat interface of IDE) |
| Server | Proces dat MCP spreekt en resources/tools aanbiedt |
| Resource | Leestoegang tot gestructureerde data (bijv. repo, backlog, config) |
| Tool | Actie die uitgevoerd kan worden (bijv. maak issue, voer query uit) |
| Prompt | Voorgedefinieerde prompt-sjabloon die server aanbiedt |
| Protocol Transport | Vaak JSON-RPC over stdio / sockets |

## 4. Architectuur (hoog niveau)
```
+-----------+        JSON-RPC        +------------------+
|  Client   | <--------------------> |   MCP Server(s)  |
| (LLM UI)  |                        |  (GitHub, DB, ..) |
+-----------+                        +------------------+
        |                                      |
        |                                   Externe
        |                                   systemen
```

Een client kan meerdere servers tegelijk verbinden (bijv. GitHub + Postgres + Filesystem).

## 5. Interactieflow (voorbeeld)
1. Client start server proces (of verbindt) via declaratie in config
2. Server stuurt capabilities (welke tools, resources, prompts)
3. Gebruiker stelt vraag → model beslist of tool/resource nodig is
4. Client vraagt resource of voert tool aanroep uit
5. Resultaat wordt teruggevoerd naar model context

## 6. GitHub MCP Server voorbeeld
We nemen een denkbeeldige GitHub MCP server die o.a. repo-bestanden kan lezen en issues kan maken.

In deze map vind je een minimalistisch pseudo-implementatie:
- `github-mcp-server.js` – startbare JSON-RPC skeleton met beperkte capabilities
- `mcp.json` – configuratie die door een client kan worden gebruikt
- `package.json` – bevat dependency `octokit`

Start test (met token geëxporteerd):
```
export GITHUB_TOKEN=ghp_XXXXXXXX
node github-mcp-server.js
```
Je zou één capabilities-regel (JSON) moeten zien.

### 6.1 Configuratievoorbeelden
`mcp.json` (client config snippet):
```json
{
  "servers": {
    "github": {
      "command": "node",
      "args": ["./github-mcp-server.js"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}" 
      }
    }
  }
}
```

### 6.2 Voorbeeld server (vereenvoudigd pseudo-JS)
```javascript
// github-mcp-server.js (schets)
import { createServer } from 'mcp-core';
import { Octokit } from 'octokit';

const octo = new Octokit({ auth: process.env.GITHUB_TOKEN });

const server = createServer({
  name: 'github',
  resources: {
    async 'repo:file'(params) { // params: { owner, repo, path }
      const res = await octo.request('GET /repos/{owner}/{repo}/contents/{path}', params);
      const content = Buffer.from(res.data.content, res.data.encoding).toString('utf8');
      return { mime: 'text/plain', data: content };
    }
  },
  tools: {
    async createIssue({ owner, repo, title, body }) {
      const issue = await octo.request('POST /repos/{owner}/{repo}/issues', { owner, repo, title, body });
      return { id: issue.data.number, url: issue.data.html_url };
    }
  },
  prompts: {
    'repo-summary': {
      description: 'Geef een samenvatting van een repo bestand',
      inputSchema: {
        type: 'object',
        properties: { owner: {type:'string'}, repo:{type:'string'}, path:{type:'string'} },
        required: ['owner','repo','path']
      }
    }
  }
});

server.start();
```

### 6.3 Voorbeeld clientaanroep (pseudo-Python)
```python
from mcp_client import MCPClient

client = MCPClient(config_path="./mcp.json")
client.connect("github")

# Resource ophalen
data = client.get_resource("github", "repo:file", {"owner": "octocat", "repo": "hello-world", "path": "README.md"})
print(data[:120])

# Tool aanroepen
issue = client.call_tool("github", "createIssue", {
    "owner": "octocat",
    "repo": "hello-world",
    "title": "Bug: fout in parser",
    "body": "Reproductie stappen ..."
})
print(issue)
```
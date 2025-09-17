"""TRYME - Praktische stappen voor gebruik van de GitHub MCP demo.

Deze file focust nu uitsluitend op instructies (de eerdere FakeMCPClient is verwijderd).

Je vindt in deze map de volgende relevante bestanden:
- github-mcp-server.js  -> Pseudo JSON-RPC server (vereenvoudigd) die beperkte GitHub acties aanbiedt
- mcp.json              -> Client configuratie voorbeeld
- package.json          -> Node project manifest (Octokit dependency)

LET OP: Dit is geen volledige officiële MCP implementatie; het demonstreert principes.

============================
STAPPENPLAN: GitHub MCP in VS Code toevoegen
============================

Let op: De exacte implementatie van MCP-integratie in VS Code kan evolueren. Dit is een generiek stappenplan dat laat zien hoe het meestal gaat.

Voorwaarden:
- Node.js geïnstalleerd (voor een voorbeeld JavaScript/TypeScript server)
- Een GitHub Personal Access Token (PAT) met minimaal 'repo' rechten (of fine-grained token)
- Een (fictief) MCP GitHub server script (bijv. `github-mcp-server.js`)

Stap 1: Maak een map voor je server
    mkdir mcp_servers/github
    cd mcp_servers/github

Stap 2: Initialiseer Node project (voorbeeld)
    npm init -y
    npm install octokit

Stap 3: Voeg serverbestand toe (vereenvoudigd voorbeeld)
    github-mcp-server.js
    ---------------------------------
    import { Octokit } from 'octokit';
    // Placeholder; in echte MCP implementeer je JSON-RPC handlers
    const octo = new Octokit({ auth: process.env.GITHUB_TOKEN });
    // Expose resources & tools via MCP server start (pseudocode)
    // startMcpServer({ resources: {...}, tools: {...} });
    ---------------------------------

Stap 4: Maak een configuratiebestand voor de client (bijv. `mcp.json` in project root)
    {
      "servers": {
        "github": {
          "command": "node",
          "args": ["./mcp_servers/github/github-mcp-server.js"],
          "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
        }
      }
    }

Stap 5: Exporteer je token in je shell (Linux/macOS)
    export GITHUB_TOKEN=ghp_XXXXXXXXXXXXXXXXXXXX

Stap 6: Start/activeer de MCP client functionaliteit
    - Afhankelijk van de IDE/extension: open de command palette en kies "MCP: Reload Servers" of vergelijkbaar.
    - Controleer logs of de server connectie maakt.

Stap 7: Gebruik in een AI chat venster
    Vraag bijvoorbeeld: "Lees het bestand README.md uit repo octocat/hello-world".
    Het model kan nu (als tooling aan staat) de resource `repo:file` opvragen via de server.

Stap 8: Issue aanmaken test
    Prompt: "Maak een GitHub issue met titel 'Bug: crash bij lege invoer' in octocat/hello-world met een beschrijving."
    Controleer in de repo of het issue is aangemaakt.

Troubleshooting tips:
- Fout: 'Permission denied' → Token scope onvoldoende.
- Server hangt → Voeg logging toe rond elke JSON-RPC message.
- Geen resources zichtbaar → Controleer dat capabilities bij start worden teruggestuurd.

Veiligheid:
- Gebruik nooit je persoonlijke all-access token in een demo.
- Gebruik fine-grained tokens en rotate ze regelmatig.
- Log geen volledige request bodies met secrets.

Uitbreiding ideeën:
- Caching van repo bestanden (ETag)
- Rate limit monitoring
- Tool toevoegen voor pull request samenvatting

============================
EINDE STAPPENPLAN
============================
"""

# Snelle start (Linux/macOS):
# 1. Exporteer een GitHub token (fine-grained waar mogelijk):
#    export GITHUB_TOKEN=ghp_XXXXXXXXXXXXXXXX
# 2. Installeer dependencies in deze map:
#    npm install
# 3. Start de server afzonderlijk (debug / handmatig test):
#    node ./github-mcp-server.js
#    Je ziet 1 JSON-regel met 'capabilities'.
# 4. (In een MCP-compatibele client of integratie) wijs naar `mcp.json`.
# 5. Vraag de AI: "Haal het bestand README.md op uit octocat/hello-world" -> model zou `getResource` aanroepen.
# 6. Vraag de AI: "Maak een issue aan in octocat/hello-world met titel 'Test Issue'" -> model zou `createIssue` tool gebruiken.

# Handmatige test zonder client (quick & dirty):
#  echo '{"jsonrpc":"2.0","id":1,"method":"getResource","params":{"name":"repo:file","params":{"owner":"octocat","repo":"hello-world","path":"README.md"}}}' | \
#  node github-mcp-server.js

# Verwacht: JSON response met base64-decoded content van README.

# Uitbreidingsideeën:
# - Retry & timeout logic toevoegen
# - Logging/metrics (bijv. pino + OpenTelemetry)
# - Meerdere resources: repo:listFiles, repo:search
# - Tools: createPR, commentIssue

# Veiligheidstip: commit nooit echte tokens. Gebruik .env + dotenv loader.

# Einde TRYME uitleg.

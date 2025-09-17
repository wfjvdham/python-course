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

https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp?tool=vscode
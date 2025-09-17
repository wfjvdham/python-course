# Overzicht van AI-taalmodellen

Dit hoofdstuk geeft een beknopt maar praktisch overzicht van populaire (generatieve) taalmodellen, wie ze ontwikkelt, typische use-cases, licenties, sterke punten en aandachtspunten. Geen oefeningen – bedoeld als naslag.

## 1. Waarom modelkeuze belangrijk is
Een goed gekozen model kan kosten verlagen, latency verbeteren, privacyrisico's beperken en kwaliteit verhogen. Factoren:
- Beschikbaarheid (open source vs closed)
- Kosten (tokens / runtime / hardware)
- Kwaliteit (redeneervermogen, factual accuracy)
- Domeinspecifiek gedrag (code, medische tekst, creatief schrijven)
- Governance & compliance (GDPR, data residency)
- Uitbreidbaarheid / fine-tuning opties

## 2. Overzicht per aanbieder
| Aanbieder | Voorbeeldmodellen | Kenmerken | Licentie / toegang |
|-----------|-------------------|-----------|--------------------|
| OpenAI | GPT-3.5, GPT-4, GPT-4o, o1 | Sterk in redeneren, brede tooling integraties | API (closed) |
| Anthropic | Claude 3 (Haiku, Sonnet, Opus) | Veiligheid/alignement focus, lange context | API (closed) |
| Google | Gemini (Nano, Pro, Ultra) | Integratie met Google ecosysteem, multimodaal | API (closed) |
| Meta | Llama 2 / Llama 3 | Open gewichtsdistributie, veel community tooling | Open (met licentievoorwaarden) |
| Mistral AI | Mistral 7B, Mixtral 8x7B, Mistral Large | Efficiënt, sterke open modellen, MoE | Open & API |
| xAI | Grok | Snelle updates, cultureel web-heavy | API (closed) |

## 3. Open vs Closed modellen
| Aspect | Open | Closed |
|--------|------|--------|
| Transparantie | Inzicht in architectuur/gewichten | Beperkt |
| Aanpasbaarheid | Fine-tuning / LoRA lokaal | Alleen via provider (soms) |
| Infrastructuur | Zelf hosten vereist | Provider regelt alles |
| Kostenstructuur | Upfront (hardware) + variabel | Pay-per-use |
| Innovatiesnelheid | Snelle community forks | Centrale roadmap |
| Privacycontrole | Volledig intern mogelijk | Vertrouwen op policies |

## 4. Typische use-cases per modeltype
| Use-case | Aanrader (voorbeeld) | Reden |
|----------|----------------------|-------|
| Code generatie | GPT-4 / Claude / Llama 3 instruct | Sterke reasoning + code context |
| Snelle goedkope chat | GPT-3.5 / Claude Haiku / Mistral 7B | Lage kosten, redelijke kwaliteit |
| Embedded/on-device | Phi-3 Mini / Llama 3 8B / Gemma | Klein, efficiënt |
| Lange documenten | Claude 3 Sonnet/Opus | Grote context windows |
| Creatief schrijven | GPT-4 / Llama 3 70B | Stijlvariatie |
| Meertalige taken | GPT-4o / Gemini | Sterke meertaligheid |

## 5. Samenvatting in één tabel
| Situatie | Aanpak |
|----------|--------|
| Start greenfield prototype | Closed premium (GPT-4/Claude) voor snelheid |
| Kosten onder druk | Downgrade naar Mistral/Llama variant |
| Privacy streng | Zelfgehost open model + RAG |
| Veel documenten | Model met groot context window |
| Complexe redenatie nodig | Claude Opus / GPT-4o / Mixtral MoE |
| Edge/device | Klein compact model (Phi / Gemma / Llama 3 8B) |

## 6. Verdere verdieping
- Hugging Face model hub voor open modellen
- Papers with Code voor benchmarks
- OpenAI / Anthropic / Google blogs voor capability updates
- Responsible AI guidelines (EU AI Act, NIST)

## 7. Disclaimer
Het landschap evolueert snel; controleer altijd actuele versies, licenties en benchmarks voordat je een keuze definitief maakt.

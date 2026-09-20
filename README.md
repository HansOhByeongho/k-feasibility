# K-Feasibility

Public development feasibility scenario calculator for demand, cost and funding.

Early-stage public-sector AI research prototype. Official data, laws and statistics must be verified against their source before decision-making.

## Scope
- API-first modular architecture
- Korean public-data integration ready
- deterministic local fallback
- no API keys, personal data, internal documents or generated reports committed

## Planned API
`GET /health` and `POST /analyze` using FastAPI. Domain: **feasibility**.

## Relationship
Independent component designed for integration with [National AI Orchestrator](https://github.com/HansOhByeongho/national-ai-orchestrator).

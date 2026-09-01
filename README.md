# clinical-ai-agent

End-to-end clinical AI agent integrating LLMs, RAG, SQL, tools, MCP and workflow automation.

## Project Overview

This project implements a modular Clinical AI Agent designed to progressively integrate:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- SQL databases
- External tools
- Model Context Protocol (MCP)
- Workflow automation

## Current Architecture

The current version includes:

- `ClinicalAIAgent` — core orchestration layer
- `LLMClient` — interface for interacting with the language model
- Query processing through the LLM layer

## Project Structure

```text
clinical-ai-agent/
│
├── src/
│   ├── agent/
│   │   └── agent.py
│   │
│   ├── llm/
│   │   └── llm.py
│   │
│   └── data/
│       └── README.md
│
├── README.md
└── .gitignore

# Repository Guidelines

This repository is a learning lab for experimenting with Python agent systems:
building agents, orchestrating long-running workflows, and evaluating and
observing their behavior. Prefer small, isolated experiments and loosely
coupled tools over production infrastructure.

- Use Python 3.12 and `uv`; prefer the `Makefile` commands.
- Keep agents in `src/agents_lab/agents/`; Prefect code in `src/agents_lab/flows/`.
- Agents must not import flows. Extract shared code only after a second use.
- Read secrets from environment variables; never commit or log values.
- Add only empty variable names to `.env.example`.
- Add dependencies and abstractions only when an experiment needs them.
- Briefly explain important choices and execution models while working.
- After each task, suggest one relevant improvement or new topic to explore.
- Separate advice to use now from ideas that are merely valuable to learn.
- Challenge assumptions with reasons; do not agree reflexively.
- Use lowercase conventional commits, at most eight words.

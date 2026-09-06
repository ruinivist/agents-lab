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
- ALWAYS prefer opting out of trainings.

# Code Guidelines

- Prefer no code: use YAGNI, reuse existing code, stdlib/native features, and installed deps before writing anything new.
- Understand the full flow first; fix root causes in shared code, not symptoms in individual callers.
- Choose the smallest boring diff: no unrequested abstractions, dependencies, boilerplate, or extra files.
- Never trade away correctness, validation, security, accessibility, data safety, or explicitly requested behavior for brevity.
- Testing: optimize for confidence, not test count—write as few tests as possible, only enough to prove the change works and catch the relevant regression; avoid redundant coverage.
- Do not mock an api to only prove that calling a mocked function returns what the mock was told to return. That is
  testing for the sake of testing.

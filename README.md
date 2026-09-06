# Agents Lab

An experiment repository for Pydantic AI agents orchestrated by Prefect.

## Setup

Python 3.12 and [`uv`](https://docs.astral.sh/uv/) are required.

```sh
make install
make hooks
```

The second command installs the local secret-scanning hook. Git does not install
repository hooks automatically, so run it once for every clone.

Run `make help` to list the available maintenance commands. Use `make update`
to update all locked dependencies.

## Structure

```text
src/agents_lab/
├── agents/  # Agent instructions, tools, and output models
└── flows/   # Prefect orchestration, retries, and schedules
```

Keep agents independent of Prefect. A flow may import and run an agent, but an
agent must not import a flow. Keep code beside its only consumer; create a
shared module only when a second real consumer appears.

Start with one module per agent or flow. Promote a module to a subpackage only
when its prompt, tools, or models no longer fit comfortably together.

## Secrets

Code receives secrets through standard environment variables. Do not hardcode
keys, commit local environment files, or build a central registry containing
every provider key.

1. Add each required variable name, with an empty value, to `.env.example`.
2. Copy `.env.example` to `.env` and put real values only in `.env`.
3. Load it explicitly when needed:

   ```sh
   uv run --env-file .env <command>
   ```

For deployed flows, inject the same environment-variable names from Prefect
Secret blocks or the execution platform's secret manager. Agent code should
never know the Prefect block name. Use Prefect Variables only for non-sensitive
configuration.

Gitleaks scans staged changes when committing.

If a real credential ever reaches Git history or a remote, revoke and rotate it
immediately. Removing it in a later commit does not make it secret again.

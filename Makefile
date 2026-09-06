.PHONY: help install update hooks

help:
	@echo "install  sync locked dependencies"
	@echo "update   update and sync dependencies"
	@echo "hooks    install local git hooks"

install:
	uv sync --locked

update:
	uv lock --upgrade
	uv sync --locked

hooks:
	uv run pre-commit install

.PHONY: help

help:
	@echo "help   : Show this help message"
	@echo "build  : Build mkdocs"
	@echo "install: Install dependencies"
	@echo "lint   : Run server"
	@echo "serve  : Run pre-commit hooks"
	@echo "gh     : Deploy to GitHub pages"
	@echo "pypi   : Deploy to pypi"

build:
	@poetry run mkdocs build

install:
	@pip install poetry
	@poetry install
	@poetry run pre-commit install

lint:
	@poetry run pre-commit run -a
serve:
	@poetry run mkdocs serve

gh:
	@poetry run mkdocs gh-deploy --clean --force

pypi:
	@poetry build
	@poetry publish
	@rm -rf dist
	@rm -rf *.egg-info

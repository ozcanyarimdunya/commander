.PHONY: help

help:
	@echo "help        : Show this help message"
	@echo "serve-docs  : Run documentation server"
	@echo "build-docs  : Build mkdocs"
	@echo "install     : Install dependencies"
	@echo "lint        : Run pre-commit hooks"
	@echo "gh-deploy   : Deploy to GitHub pages"
	@echo "publish-pypi: Deploy to pypi"
	@echo "test        : Run tests"

serve-docs:
	@poetry run mkdocs serve

build-docs:
	@poetry run mkdocs build

install:
	@poetry install
	@poetry run pre-commit install

lint:
	@poetry run pre-commit run -a

gh-deploy:
	@poetry run mkdocs gh-deploy --clean --force

publish-pypi:
	@poetry build
	@poetry config pypi-token.pypi $(PYPI_TOKEN)
	@poetry publish --dry-run
	@poetry publish
	@rm -rf dist
	@rm -rf *.egg-info

test:
	@poetry run pytest --cov

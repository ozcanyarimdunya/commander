.PHONY: help

help:
	@echo "help   : Show this help message"
	@echo "build  : Build mkdocs"
	@echo "install: Install dependencies"
	@echo "serve  : Run server"
	@echo "publish: Deploy to GitHub pages"
	@echo "package: Deploy to pypi"

build:
	@mkdocs build

install:
	@pip install -r dev-requirements.txt

serve:
	@mkdocs serve

publish:
	@mkdocs gh-deploy --clean --force

package:
	@rm -rf dist
	@rm -rf *.egg-info
	@python setup.py sdist
	@twine upload --skip-existing dist/*
	@rm -rf dist
	@rm -rf *.egg-info

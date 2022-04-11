.PHONY: help

help:
	@echo "help   : Show this help message"
	@echo "build  : Build mkdocs"
	@echo "install: Install dependencies"
	@echo "serve  : Run server"
	@echo "publish: Deploy to GitHub pages"

build:
	@mkdocs build

install:
	@pip install -r requirements.txt

serve:
	@mkdocs serve

publish:
	@mkdocs gh-deploy --clean --force

package:
	@python setup.py sdist
	@twine upload dist/*
	@rm -rf dist
	@rm -rf *.egg-info

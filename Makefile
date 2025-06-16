PYTHONPATH = PYTHONPATH=./
POETRY_RUN = poetry run
OPEN_API_GENERATE = openapi-generator-cli generate

YAML_FILE = openapi/autofollow.yml
OUT = ./
PACKAGE_DIR = ttech_autofollow

MAIN_CODE = tests examples ttech_autofollow

.PHONY: lint
lint:
	$(POETRY_RUN) ruff check $(MAIN_CODE)
	$(POETRY_RUN) black --check $(MAIN_CODE)
	$(POETRY_RUN) mypy $(MAIN_CODE)
	$(POETRY_RUN) poetry check

.PHONY: format
format:
	$(POETRY_RUN) isort $(MAIN_CODE)
	$(POETRY_RUN) black $(MAIN_CODE)
	$(POETRY_RUN) ruff check --fix $(MAIN_CODE)

.PHONY: install-poetry
install-poetry:
	pip install poetry

.PHONY: install
install:
	poetry install -E all

.PHONY: publish
publish:
	@poetry publish --build --no-interaction --username=$(pypi_username) --password=$(pypi_password)

.PHONY: gen-api
gen-api:
	#rm -r ${PACKAGE_DIR}
	${OPEN_API_GENERATE} -i ${YAML_FILE} -g python -o ${OUT} \
	--additional-properties=packageName=ttech_autofollow,generateSourceCodeOnly=true \
	--ignore-file-override .openapi-generator-ignore \
	--global-property=apiDocs=false,modelDocs=flase,apiTests=false,modelTests=false

.PHONY: gen-client
gen-client: gen-api

.PHONY: update-version
update-version:
	$(POETRY_RUN) python -m scripts.update_version

.PHONY: update
update: gen-client format lint update-version

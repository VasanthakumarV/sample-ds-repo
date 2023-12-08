PDM := "pdm run"

# Install all dependencies
install:
	pdm install

# Unit-test sql and python files
test *ARGS:
	{{ PDM }} pytest {{ ARGS }}

# Format all sql and python files
fmt:
	{{ PDM }} sqlfluff format --dialect postgres --ignore templating .
	{{ PDM }} ruff format .

# Install dependencies relevant for CI
ci-install:
	# TODO deps for linting, testing and mypy must be separated
	# and they should be run parallely in ci
	pdm install

ci-lint: ci-ruff ci-mypy ci-sql

ci-ruff:
	{{ PDM }} ruff check --no-fix .
	{{ PDM }} ruff format --diff .

ci-mypy:
	{{ PDM }} mypy .

ci-sql:
	{{ PDM }} sqlfluff lint --dialect postgres --ignore templating .

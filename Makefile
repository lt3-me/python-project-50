lint:
	poetry run flake8 gendiff

test:
	poetry run pytest 

test-local:
	poetry run python3 -m pytest

install:
	poetry install

check:
	make lint
	make test

test-coverage:
	poetry run python3 -m pytest --cov=gendiff --cov-report=html
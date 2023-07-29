lint:
	poetry run flake8 gendiff

install:
	poetry install

check:
	make lint

test-coverage:

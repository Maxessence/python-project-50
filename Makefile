install:
	poetry install

publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests/gendiff_test.py

selfcheck:
	poetry check

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check: lint selfcheck test

build: check
	poetry build
	
		
.PHONY: install lint selfcheck test build

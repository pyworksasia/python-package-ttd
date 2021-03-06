# Python Package TDD Template

A sample python package template with Test Driven Development (TDD).

## Quickstart

Create virtualenv with Python 3

```shell
virtualenv -p python3 venv
```

Run testing

```shell
pytest
# OR
pytest --durations=3 -vv --cov
# OR
make test
```

Test Coverage

Coverage to the test will be config in .coveragerc file.

- include: Will be aply coverage for our project in myproj only, it will ignore all other dir like venv, etc...

```shell
[run]
branch = True
include =
    myproj/*
```

## Learn more about Pytest 

- pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.

## Reference

- https://docs.pytest.org/en/stable/getting-started.html

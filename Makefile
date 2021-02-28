test:
	pytest --durations=3 -vv

test-cov:
	pytest --durations=3 -vv --cov-config=.coveragerc --cov-report html --cov
.PHONY: lint format test all

lint:
    pylint . 

format:
    black .

test:
    pytest 

all: lint format test

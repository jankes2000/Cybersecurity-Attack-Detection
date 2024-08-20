.PHONY: lint format security all

lint:
	pylint ./mlops --exit-zero

format:
	black ./mlops

security:
	bandit -r ./mlops

all: lint format security

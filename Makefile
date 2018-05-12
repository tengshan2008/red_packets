init:
	pip install -r requirments.txt
test:
	py.test tests
PHONY: init test
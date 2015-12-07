
test:
	nosetests

linter:
	pep8 --ignore=E251 .

.PHONY: test linter

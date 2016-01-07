test:
	python3.5 -m nose

install:
	python3.5 -m pip install . --upgrade

run-help:
	python3.5 -m astexport --help

linter:
	pep8 --ignore=E251 .

dist-upload: clean linter test
	python setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info/
	rm -rf */__pycache__

.PHONY: test linter dist-upload clean

test:
	nosetests-3.4

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

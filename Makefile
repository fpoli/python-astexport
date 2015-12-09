
test:
	nosetests

linter:
	pep8 --ignore=E251 .

dist-upload:
	python setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	rm -rf dist
	rm -rf *.egg-info/

.PHONY: test linter dist-upload clean

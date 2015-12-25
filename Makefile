.DEFAULT_GOAL := all

.PHONY: all
all: install-prepush lint

.PHONY: lint
lint:
	pep8 aprsclient/ ./*.py
	pylint --rcfile=.pylintrc aprsclient/ ./*.py

.PHONY: install-prepush
install-prepush:
	@-if [ -d .git ] && [ ! -h .git/hooks/pre-push ] ; then \
		ln -s ../../prepush .git/hooks/pre-push; \
	fi

.PHONY: clean
clean:
	find . -name \*.pyc -delete

.PHONY: test
test: clean lint
	nosetests $(find . -name "_test.py")

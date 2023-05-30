.PHONY: clean
clean:
	trash ./*.egg-info
	trash ./dist
	trash ./build

.PHONY: git-clean-check
git-clean-check:
	@echo "\n*** Checking that everything is committed**"
	@if [ -n "$(shell git status -s)" ]; then\
		echo "git status is not clean. You have uncommitted git files";\
		exit 1;\
	else\
		echo "git status is clean";\
    fi

.PHONY: build
build: git-clean-check
	python setup.py sdist bdist_wheel

.PHONY: upload
upload:
	twine upload dist/*

.PHONY: publish
publish: clean build upload

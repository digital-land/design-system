include makerules/makerules.mk


# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

all:: render

init::
	pip3 install --upgrade pip
	pip3 install --upgrade -r requirements.txt
	npm install


lint:	black-check flake8

black:
	black .

black-check:
	black --check .

flake8:
	flake8 .

dist:
	mkdir -p docs/static

clobber::
	rm -rf docs

render: dist
	python3 render.py

render/local: dist
	python3 render.py --local

images:
	cp -r documentation/digital-land/components/timeline/images docs/components/timeline

server:
	python -m http.server --directory docs/

commit-docs::
	git add docs
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt design system $(shell date +%F)"; git push origin $(BRANCH))

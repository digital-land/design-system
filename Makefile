include makerules/makerules.mk


# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

all:: render

init::
	pip3 install --upgrade pip
	pip3 install --upgrade -r requirements.txt

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

# should point to local version of frontend
FRONTEND=../frontend

latest/css:
	cd $(FRONTEND) && gulp stylesheets
	rsync -r $(FRONTEND)/digital_land_frontend/static/stylesheets/ docs/static/stylesheets/

latest/js:
	cd $(FRONTEND) && gulp js
	rsync -r $(FRONTEND)/digital_land_frontend/static/javascripts/ docs/static/javascripts/

local: render/local latest/js latest/css

local/css:
	mkdir -p docs/static/stylesheets
	wget -O docs/static/stylesheets/dl-frontend.css https://raw.githubusercontent.com/digital-land/frontend/master/digital_land_frontend/static/stylesheets/dl-frontend.css

local/js:
	mkdir -p docs/static/javascripts/govuk
	wget -O docs/static/javascripts/govuk/govuk-frontend.min.js https://raw.githubusercontent.com/digital-land/frontend/master/digital_land_frontend/static/javascripts/govuk/govuk-frontend.min.js
	wget -O docs/static/javascripts/dl-frontend.js https://raw.githubusercontent.com/digital-land/frontend/master/digital_land_frontend/static/javascripts/dl-frontend.js


commit-docs::
	git add docs
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt design system $(shell date +%F)"; git push origin $(BRANCH))

# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

init: submodule
	pip3 install --upgrade -r requirements.txt
	cd frontend && pip install -e . && npm install

submodule:
	git submodule update --init --recursive --remote

render:
	python3 render.py

render/local:
	python3 render.py --local

images:
	cp -r src/digital-land/components/timeline/images docs/components/timeline

latest/css:
	cd frontend && gulp stylesheets
	rsync -r frontend/digital_land_frontend/static/stylesheets/ docs/static/stylesheets/

latest/js:
	cd frontend && gulp js
	rsync -r frontend/digital_land_frontend/static/javascripts/ docs/static/javascripts/

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
	git diff --quiet && git diff --staged --quiet || (git commit -m "Rebuilt docs $(shell date +%F)"; git push origin $(BRANCH))
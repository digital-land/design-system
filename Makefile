init: submodule
	pip3 install --upgrade -r requirements.txt

submodule:
	git submodule update --init --recursive

render:
	python3 render.py

images:
	cp -r src/digital-land/components/timeline/images docs/components/timeline

local/css:
	mkdir -p docs/static/stylesheets
	wget -O docs/static/stylesheets/dl-frontend.css https://raw.githubusercontent.com/digital-land/frontend/master/digital_land_frontend/static/stylesheets/dl-frontend.css

local/js:
	mkdir -p docs/static/javascripts/govuk
	wget -O docs/static/javascripts/govuk/govuk-frontend.min.js https://raw.githubusercontent.com/digital-land/frontend/master/digital_land_frontend/static/javascripts/govuk/govuk-frontend.min.js
	wget -O docs/static/javascripts/dl-frontend.js https://raw.githubusercontent.com/digital-land/frontend/master/digital_land_frontend/static/javascripts/dl-frontend.js
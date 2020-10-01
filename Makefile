init: 
	git submodule update --init --recursive
	pip3 install --upgrade -r requirements.txt

render:
	python3 render.py

VENV_PATH = ./venv
VENV = . $(VENV_PATH)/bin/activate;
CONFIG_DIR = $(HOME)/.config/vpn_dns_changer
CONFIG_PATH = $(CONFIG_DIR)/config.json

SRC := \
	$(wildcard vpn_dns_changer_lib/*.py) \
	$(wildcard scripts/*)

clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist

build: dist/

copy-config: $(CONFIG_PATH)

configure:
	python3 -m venv $(VENV_PATH)
	$(VENV) pip install -r requirements.txt

install: dist/ $(CONFIG_PATH)
	pip3 install .

install-venv: dist/
	$(VENV) pip install .

$(CONFIG_PATH): config.json
	mkdir -p $(CONFIG_DIR)
	rm -f $(CONFIG_PATH)
	cp config.json $(CONFIG_PATH)

dist/: $(VENV_PATH) $(SRC)
	$(VENV) python3 setup.py sdist bdist_wheel
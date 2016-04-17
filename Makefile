DEFAULT: help

#
VE_DIR = venv
BIN_DIR = $(VE_DIR)/bin
PYTHON_CMD = $(BIN_DIR)/python
PIP_CMD = $(BIN_DIR)/pip
#
SYS_PYTHON = python2


setup:
	sudo apt-get install --yes python-virtualenv
	sudo apt-get install --yes python-dev

dev:
	virtualenv --python $(SYS_PYTHON) $(VE_DIR)
	$(PIP_CMD) install -r requirements.txt
	$(PYTHON_CMD) setup.py install

clean:
	rm -rf $(VE_DIR)

help:
	@echo "Choose from the following:"
	@echo "	setup	Setup a new box"

# End of file.

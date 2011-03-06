PREFIX = /usr/local
EXEC_DIR = $(PREFIX)/bin

all: install

install:
	install -m 0775 djake $(EXEC_DIR)/djake

uninstall:
	-rm -f $(EXEC_DIR)/djake

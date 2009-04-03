PREFIX = /usr/local
EXEC_DIR = $(PREFIX)/bin

all: install

clean:
	rm -f django-manage.pyc

install:
	install -m 0775 django-manage.py $(EXEC_DIR)/django-manage.py

run:
	python django-manage.py

uninstall:
	-rm -f $(EXEC_DIR)/django-manage.py

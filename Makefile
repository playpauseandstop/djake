PREFIX = /usr/local
EXEC_DIR = $(PREFIX)/bin

all: install

run:
	python django-manage.py

install:
	install -m 0775 django-manage.py $(EXEC_DIR)/django-manage.py

clean:
	rm -f django-manage.pyc

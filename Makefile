mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

lokal:
	python3 manage.py makemessages -l en
	python3 manage.py makemessages -l ru
	python3 manage.py makemessages -l uz
run:
	python3 manage.py runserver
compile:
	python3 manage.py compilemessages

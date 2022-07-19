test:
	poetry run pytest exercise

lint:
	poetry run pre-commit

local-run:
	poetry run python exercise/manage.py runserver

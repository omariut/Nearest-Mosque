export $(xargs <./.env)
pip install requirements.txt
python manage.py makemigration
python manage.py migrate
python manage.py runserver

web: gunicorn BackEnd_GeoSport.wsgi
release: python manage.py makemigration --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput

#!/bin/sh

# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python manage.py makemigrations --noinput
python manage.py migrate --run-syncdb --noinput
python manage.py collectstatic --noinput

echo "Creating superuser"
python manage.py createsuperuser --noinput || true

exec "$@"
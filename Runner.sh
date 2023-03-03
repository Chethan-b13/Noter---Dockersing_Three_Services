#!/bin/bash
docker-compose up --build -d
echo "what's the container's index"
read INDEX
echo "making migrations docker exec -it chethan_django_$INDEX"
docker exec -it chethan_django_$INDEX /bin/sh -c "python manage.py makemigrations && python manage.py migrate"
docker exec -it chethan_flask_$INDEX /bin/sh -c "python - <<EOF
from app import db,app
with app.app_context():
    db.create_all()
EOF
"

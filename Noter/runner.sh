python -c "python - <<EOF
from app import db,app
with app.app_context():
    db.create_all()
EOF
"

python app.py
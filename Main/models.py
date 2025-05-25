from Main import db

class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(), nullable=False, unique=False)
    phone = db.Column(db.String(), nullable=False, unique=False)
    feedback = db.Column(db.Text, nullable=False)
    
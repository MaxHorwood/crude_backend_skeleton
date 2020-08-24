from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    addresses = db.relationship("Address", backref="user", lazy=True)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postcode = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

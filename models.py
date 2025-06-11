from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class SEORequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    score = db.Column(db.Integer)
    score_out_of = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # SEO details
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    h1 = db.Column(db.String(255))
    h1_count = db.Column(db.Integer)
    image_alt_ratio = db.Column(db.String(50))
    robots = db.Column(db.String(100))
    canonical = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref="seo_requests")
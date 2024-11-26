from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class Report(db.Model):
    __tablename__ = 'reports'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    query = db.Column(db.JSON, nullable=False)
    generated_data = db.Column(db.JSON, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "query": self.query,
            "generated_data": self.generated_data
        }

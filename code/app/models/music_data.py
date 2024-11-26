from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class MusicData(db.Model):
  __tablename__ = 'music_data'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(255), nullable=False)
  artist = db.Column(db.String(255), nullable=False)
  genre = db.Column(db.String(100), nullable=False)
  region = db.Column(db.String(100), nullable=False)
  sales = db.Column(db.Integer, nullable=False)
  streams = db.Column(db.Integer, nullable=False)
  release_date = db.Column(db.Date, nullable=False)

  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "artist": self.artist,
      "genre": self.genre,
      "region": self.region,
      "sales": self.sales,
      "streams": self.streams,
      "release_date": self.release_date.isoformat()
    }

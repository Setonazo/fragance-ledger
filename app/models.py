from datetime import datetime

from .extensions import db


class Fragrance(db.Model):
    __tablename__ = "fragrances"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    brand = db.Column(db.String(120), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    season = db.Column(db.String(40), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<Fragrance {self.brand} - {self.name}>"

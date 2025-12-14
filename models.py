from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.String(50), unique=True, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "bus_id": self.bus_id,
            "latitude": self.latitude,
            "longitude": self.longitude
        }

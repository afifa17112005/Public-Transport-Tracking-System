from app import create_app
from models import db, Bus

app = create_app()

with app.app_context():
    db.create_all()
    # Add some buses if database is empty
    if Bus.query.count() == 0:
        buses = [
            Bus(bus_id="Bus-1", latitude=12.9716, longitude=77.5946),
            Bus(bus_id="Bus-2", latitude=12.9616, longitude=77.5846),
            Bus(bus_id="Bus-3", latitude=12.9816, longitude=77.6046),
        ]
        db.session.add_all(buses)
        db.session.commit()
        print("Database initialized with sample buses")

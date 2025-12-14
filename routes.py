from flask import Blueprint, jsonify, request, render_template
from models import db, Bus

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return "Bus Tracking API is running!"

@main_routes.route('/map')
def map_view():
    return render_template('index.html')

@main_routes.route('/buses')
def get_buses():
    buses = Bus.query.all()
    return jsonify([bus.to_dict() for bus in buses])

@main_routes.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    bus_id = data.get('bus_id')
    bus = Bus.query.filter_by(bus_id=bus_id).first()
    if not bus:
        return jsonify({"error": "Bus not found"}), 404

    bus.latitude = data.get('latitude', bus.latitude)
    bus.longitude = data.get('longitude', bus.longitude)
    db.session.commit()
    return jsonify({"message": "Location updated"})

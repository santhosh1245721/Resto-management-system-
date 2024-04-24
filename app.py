# restaurant_management_system.py

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/restaurant_management_system"
mongo = PyMongo(app)

# Define collections
orders_collection = mongo.db.orders
menu_collection = mongo.db.menu
tables_collection = mongo.db.tables

# API Endpoints

@app.route("/orders", methods=["GET"])
def get_orders():
    orders = orders_collection.find()
    return jsonify([order for order in orders])

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    order = orders_collection.insert_one(data)
    return jsonify({"message": "Order created successfully"})

@app.route("/menu", methods=["GET"])
def get_menu():
    menu = menu_collection.find()
    return jsonify([item for item in menu])

@app.route("/menu", methods=["POST"])
def create_menu_item():
    data = request.get_json()
    menu_item = menu_collection.insert_one(data)
    return jsonify({"message": "Menu item created successfully"})

@app.route("/tables", methods=["GET"])
def get_tables():
    tables = tables_collection.find()
    return jsonify([table for table in tables])

@app.route("/tables", methods=["POST"])
def create_table():
    data = request.get_json()
    table = tables_collection.insert_one(data)
    return jsonify({"message": "Table created successfully"})

if __name__ == "__main__":
    app.run(debug=True)

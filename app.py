from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/restaurant_management"
mongo = PyMongo(app)

@app.route("/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = mongo.db.restaurants.find()
    return jsonify([{"id": str(restaurant["_id"]), "name": restaurant["name"], "address": restaurant["address"]} for restaurant in restaurants])

@app.route("/restaurants", methods=["POST"])
def create_restaurant():
    data = request.get_json()
    restaurant = mongo.db.restaurants.insert_one({"name": data["name"], "address": data["address"]})
    return jsonify({"id": str(restaurant.inserted_id)})

@app.route("/restaurants/<id>", methods=["GET"])
def get_restaurant(id):
    restaurant = mongo.db.restaurants.find_one({"_id": ObjectId(id)})
    if restaurant:
        return jsonify({"id": str(restaurant["_id"]), "name": restaurant["name"], "address": restaurant["address"]})
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@app.route("/restaurants/<id>", methods=["PUT"])
def update_restaurant(id):
    data = request.get_json()
    restaurant = mongo.db.restaurants.update_one({"_id": ObjectId(id)}, {"$set": {"name": data["name"], "address": data["address"]}})
    if restaurant.modified_count > 0:
        return jsonify({"message": "Restaurant updated successfully"})
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@app.route("/restaurants/<id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = mongo.db.restaurants.delete_one({"_id": ObjectId(id)})
    if restaurant.deleted_count > 0:
        return jsonify({"message": "Restaurant deleted successfully"})
    else:
        return jsonify({"error": "Restaurant not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

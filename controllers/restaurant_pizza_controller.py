from flask import Blueprint, request, jsonify
from ..models.restaurant_pizza import RestaurantPizza
from ..models.restaurant import Restaurant
from ..models.pizza import Pizza
from ..config import db

restaurant_pizza_bp = Blueprint("restaurant_pizza_bp", __name__)

@restaurant_pizza_bp.route("/restaurant_pizzas", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")

    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return jsonify({"errors": ["Invalid restaurant or pizza ID"]}), 400

    new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(new_rp)
    db.session.commit()

    return jsonify({
        "id": new_rp.id,
        "price": new_rp.price,
        "pizza_id": pizza.id,
        "restaurant_id": restaurant.id,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }), 201

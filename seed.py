from .config import db 
from .app import create_app

# Create the Flask app context
app = create_app()

# Use relative imports from the same 'server' package
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create Restaurants
    r1 = Restaurant(name="Mario's", address="123 Main St")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Side Rd")

    # Create Pizzas
    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Nyama Supreme", ingredients="Beef, Onions, Cheese, Sauce")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    # Create RestaurantPizzas
    rp1 = RestaurantPizza(price=5, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=10, restaurant_id=r2.id, pizza_id=p2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("✅ Seeded successfully.")

# This script seeds the database with initial data for testing purposes.
from flask import Flask
from .config import setup_db
from .controllers.restaurant_controller import restaurant_bp
from .controllers.pizza_controller import pizza_bp
from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

def create_app():
    app = Flask(__name__)
    setup_db(app)

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
# This is the main entry point for the Flask application.
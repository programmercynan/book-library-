# → used to create a Flask web application.
from flask import Flask
# → lets Flask work with databases using SQLAlchemy (ORM).
from flask_sqlalchemy import SQLAlchemy
# → loads the configuration settings (like the database URL).
from .config import Config

# → initializes the SQLAlchemy extension (not linked to Flask yet).
db = SQLAlchemy()

# → function that sets up and returns a Flask app (factory pattern).
def create_app():
    # → creates the Flask application.
    app = Flask(__name__)
    # → loads configuration into the app.
    app.config.from_object(Config)
    # → connects the SQLAlchemy object with the Flask app.
    db.init_app(app)

# → loads a Blueprint that has app routes (URLs).
    from .routes import main
    # → tells Flask to use the routes defined in the Blueprint.
    app.register_blueprint(main)

#  → returns the ready-to-use Flask app.

    return app


"""
✅ Summary of What This File Does

    This file defines how to create and set up a Flask app.

    It configures the app, connects it to a database, and registers routes.

    Uses a clean design called the Application Factory pattern (recommended in big apps).
"""

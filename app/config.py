import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


## ✅ Summary of What This File Does

# This small script is preparing configuration for a Flask web application that uses a database. It:

    #Loads secret values (like your database URL) from a .env file.

    #Creates a Config class with settings, especially for SQLAlchemy (a Python ORM used with Flask).
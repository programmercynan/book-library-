# lets me interact with the operating systems, like reading environment variables.
import os
# loads environment variables from a .env file into python.
from dotenv import load_dotenv

#  → runs the function that reads the .env file and adds its values to the environment.
load_dotenv()

#  → defines a class to store app settings (like database URLs, flags, etc.)
class Config:
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

""" SQLALCHEMY_TRACK_MODIFICATIONS = False 
→ turns off tracking of object changes in SQLAlchemy to save resources.
"""

"""
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') 
→ reads the database connection URL from the environment.

"""


## ✅ Summary of What This File Does

# This small script is preparing configuration for a Flask web application that uses a database. It:

    #Loads secret values (like your database URL) from a .env file.

    #Creates a Config class with settings, especially for SQLAlchemy (a Python ORM used with Flask).
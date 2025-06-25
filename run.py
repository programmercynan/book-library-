"""
Perfect! 🔥 You're now looking at the entry point of your Flask application — the file you run to start your app and create the database. This is usually your main.py or run.py.
"""
from app import create_app, db
from app.models import Book # imports the book model to create its table 

app = create_app() # creates and configures the Flask app using the factory function.

if __name__ == '__main__': # runs the app only if this file is the main script.
    with app.app_context(): # sets up the environment so Flask can talk to the database.
        db.create_all() # creates tables in the database based on the models 
    app.run(debug=True)


"""
✅ Summary of What This File Does

    Sets up and starts your Flask application.

    Creates your database tables before the app runs.

    Runs the app with debugging enabled.
"""
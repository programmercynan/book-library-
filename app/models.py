# → imports the SQLAlchemy object so I can define database models.
from . import db

"""
class Book(db.Model) → defines a table called 'book' in the database.
Each instance = 1 row in that table.

"""

"""
. id = db.Column(db.Integer, primary_key=True)

✅ What it does:
Creates a column named id:

    It's an integer.

    It's the primary key, meaning it's unique and auto-increments (used to identify each row).
"""
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        # return { ... } → gives all the book details in a format that can be used in web responses.
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year
        }
    
    """
    ✅ Summary of What This File Does

    Defines a Book model = 1 table in your database.

    Each instance of Book = 1 row in the table.

    It includes a method to convert the data to a dictionary for API use.
    """

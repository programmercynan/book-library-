"""
Awesome! 🎉 You're now looking at routes — this is where the API is built. You're defining the paths (URLs) that allow users to interact with your app (like adding, viewing, updating, and deleting books).
"""
from flask import Blueprint, request, jsonify
from .models import Book
from . import db

"""
✅ What it does:
Creates a Blueprint named main, which allows you to organize routes in different files instead of putting everything in one place.

📝 Write this:

main = Blueprint('main', __name__)
→ creates a group of routes (Blueprint) to keep code organized.

"""
main = Blueprint('main', __name__)

@main.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], year=data['year'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@main.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@main.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict()), 200

@main.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.title = data['title']
    book.author = data['author']
    book.year = data['year']
    db.session.commit()
    return jsonify(book.to_dict()), 200

@main.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204


"""
✅ Summary: What This File Does

This file creates a REST API for managing books. The routes allow you to:

    ✅ Add a book (POST /books)

    ✅ View all books (GET /books)

    ✅ View a single book by ID (GET /books/<id>)

    ✅ Update a book (PUT /books/<id>)

    ✅ Delete a book (DELETE /books/<id>)
"""
from flask_security import UserMixin, RoleMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model, UserMixin):
    ___tablename___ ="user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean())
    last_visited = db.Column(db.DateTime(), default=datetime.now(), nullable=True)
    fs_uniquifier = db.Column(db.String(128), unique=True)
    roles = db.relationship('Role', secondary='userroles', backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    __tablename__="role"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

class UserRoles(db.Model):
    __tablename__='userroles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))


class Section(db.Model):
    __tablename__='section'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
    description = db.Column(db.String(255), nullable=False)

class Book(db.Model):
    __tablename__='book'
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String, nullable=False)
    date_issued = db.Column(db.DateTime(),default=datetime.now(),nullable = False)
    date_expired = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
    section_id = db.Column(db.Integer(), db.ForeignKey('section.id', ondelete='CASCADE'))
    section = db.relationship('Section', backref=db.backref('books', lazy='dynamic'))

class BookRequests(db.Model):
    __tablename__='bookrequests'
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    book_id = db.Column(db.Integer(), db.ForeignKey('book.id', ondelete='CASCADE'))
    date_requested = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
    date_returned = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')
    user = db.relationship('User', backref=db.backref('bookrequests', lazy='dynamic'))
    book = db.relationship('Book', backref=db.backref('bookrequests', lazy='dynamic'))


class Rating(db.Model):
    __tablename__='rating'
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    book_id = db.Column(db.Integer(), db.ForeignKey('book.id', ondelete='CASCADE'))
    rating = db.Column(db.Integer(), nullable=False)
    review = db.Column(db.String(255), nullable=False)
    date_rated = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
    user = db.relationship('User', backref=db.backref('ratings', lazy='dynamic'))
    book = db.relationship('Book', backref=db.backref('ratings', lazy='dynamic'))
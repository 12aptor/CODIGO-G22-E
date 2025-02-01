from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

app = Flask(__name__)
db = SQLAlchemy()

# 'postgresql://user:password@host:port/dbname'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-sqlalchemy'

db.init_app(app)

class UserModel(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime, default=func.now())

# class UserModel(db.Model):
#     __tablename__ = 'users'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100), nullable=False)
#     email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
#     created_at: Mapped[str] = mapped_column(DateTime, default=func.now())

with app.app_context():
    db.create_all()

@app.get('/users/create')
def create_user():
    user = UserModel(name='John Doe', email='john@gmail.com')
    db.session.add(user)
    db.session.commit()
    return 'User created successfully'

@app.get('/users')
def users():
    users = UserModel.query.all()
    response = []
    for user in users:
        response.append({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'created_at': str(user.created_at)
        })
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
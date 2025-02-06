from db import db
from sqlalchemy import Column, Integer, String, DateTime, func

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
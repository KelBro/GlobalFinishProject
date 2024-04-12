# import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Student(SqlAlchemyBase):
    __tablename__ = 'students'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    fio = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    # created_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                  default=datetime.datetime.now)
    request = orm.relationship("Request", back_populates='student')

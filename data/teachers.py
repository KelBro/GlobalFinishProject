import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Teacher(SqlAlchemyBase):
    __tablename__ = 'teachers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    fio = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    club_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("clubs.id"), nullable=True)
    # created_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                  default=datetime.datetime.now)

    clubs = orm.relationship("Clubs", back_populates='teacher')
    club = orm.relationship('Clubs')

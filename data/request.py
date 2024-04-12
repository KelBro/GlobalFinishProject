import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Request(SqlAlchemyBase):
    __tablename__ = 'request'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_student = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("students.id"), nullable=True)
    id_club = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("clubs.id"), nullable=True)
    is_approved = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    student = orm.relationship('Student')
    club = orm.relationship('Clubs')

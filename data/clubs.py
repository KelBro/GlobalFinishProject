import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase

class Clubs(SqlAlchemyBase):
    # Указываем название таблицы в базе данных
    __tablename__ = 'clubs'

    # Определяем столбцы таблицы и их типы данных
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    teacher_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_closed = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)
    about = sqlalchemy.Column(sqlalchemy.String)

    # teacher = orm.relationship('Teacher')
    # request = orm.relationship("Request", back_populates='club')
    # teachers = orm.relationship("Teacher", back_populates='club')

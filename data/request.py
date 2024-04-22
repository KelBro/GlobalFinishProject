import sqlalchemy
from sqlalchemy import orm

# Импорт базового класса моделей
from .db_session import SqlAlchemyBase


# Создание класса модели
class Request(SqlAlchemyBase):
    # Указываем название таблицы в базе данных
    __tablename__ = 'request'

    # Определение столбцов таблицы и их типы данных
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_student = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("students.id"), nullable=True)
    id_club = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("clubs.id"), nullable=True)
    is_approved = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    # Определение отношений между таблицами
    student = orm.relationship('Student')
    club = orm.relationship('Clubs')

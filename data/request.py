import sqlalchemy

# Импорт базового класса моделей
from .db_session import SqlAlchemyBase


# Создание класса модели
class Request(SqlAlchemyBase):
    # Указываем название таблицы в базе данных
    __tablename__ = 'request'

    # Определение столбцов таблицы и их типы данных
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    student = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name_club = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    information = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_approved = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=None)
    id_student = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

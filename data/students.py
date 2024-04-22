import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

# Импорт базового класса моделей
from .db_session import SqlAlchemyBase


# Определение класса модели Student, наследующегося от SqlAlchemyBase и UserMixin
class Student(SqlAlchemyBase, UserMixin):
    # Указываем название таблицы в базе данных
    __tablename__ = 'students'

    # Определение столбцов таблицы и их типов данных
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_teacher = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)
    name_club = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    have_club = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)
    # created_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                  default=datetime.datetime.now)
    # request = orm.relationship("Request", back_populates='student')

    # Определение метода для установки хэша пароля
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    # Определение метода для проверки пароля
    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

# Создание базового класса для всех моделей
SqlAlchemyBase = orm.declarative_base()

# Глобальная переменная для сессий
__factory = None


# Функция для инициализации подключения к базе данных
def global_init(db_file):
    global __factory

    # Если фабрика уже инициализирована, выходим из функции
    if __factory:
        return

    # Проверяем, был ли указан файл базы данных
    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    # Строка подключения к базе данных SQLite
    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)

    # Создание сессий
    __factory = orm.sessionmaker(bind=engine)

    # Импортируем все модели
    from . import __all_models

    # Создание всех таблиц в базе данных, если они еще не существуют
    SqlAlchemyBase.metadata.create_all(engine)


# Функция для создания новой сессии базы данных
def create_session() -> Session:
    global __factory
    # Возвращаем новую сессию
    return __factory()

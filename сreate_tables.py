from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from models import Base, Student, Group, Teacher, Subject, StudentMark

# Создаем соединение с базой данных
engine = create_engine('postgresql://postgres:password@localhost:5432/university')

# Создаем таблицы
Base.metadata.create_all(engine)

# Получаем инспектор для базы данных
inspector = inspect(engine)

# Получаем список таблиц
tables = inspector.get_table_names()

# Выводим список таблиц
print("Tables created:", tables)

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Закрываем сессию
session.close()

# Закрываем соединение
engine.dispose()

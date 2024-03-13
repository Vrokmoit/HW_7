from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from my_select import *

# Створення сесії
engine = create_engine('postgresql://postgres:password@localhost:5432/university')
Session = sessionmaker(bind=engine)
session = Session()

print("1. Знайти 5 студентів з найвищим середнім балом з усіх предметів:")
print(select_1(session))
print()

print("2. Знайти студента з найвищим середнім балом з певного предмету:")
print(select_2(session))
print()

print("3. Знайти середній бал груп за певним предметом:")
print(select_3(session))
print()

print("4. Знайти середній бал усіх оцінок:")
print(select_4(session))
print()

print("Курсы, читаемые Антоном Сичем:")
print(select_5(session))
print()

print("Список студентов в группе 'вечір':")
print(select_6(session))
print()

print("Оценки студентов в группе 'вечір' по предмету 'кпсс':")
print(select_7(session))
print()

print("Средний балл, выставляемый Антоном Сичем по его предметам:")
print(select_8(session))
print()

print("Список курсов, которые посещает студент Демид Колодуб:")
print(select_9(session))
print()

print("Список курсов, которые читает Антон Сич для студента Демида Колодуба:")
print(select_10(session))
print()

# Закриття сесії
session.close()

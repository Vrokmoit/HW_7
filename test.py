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

print("5. Знайти курси, які веде викладач:")
print(select_5(session))
print()

print("6. Знайти список студентів у певній групі:")
print(select_6(session))
print()

print("7. Знайти оцінки студентів у певній групі за певний предмет:")
print(select_7(session))
print()

print("8. Знайти середній бал, який ставить викладач зі своїх предметів:")
print(select_8(session))
print()

print("9. Знайти список курсів, які відвідує певний студент:")
print(select_9(session))
print()

print("10. Знайти курси, які відвідує певний студент з викладачем:")
print(select_10(session))
print()

# Закриття сесії
session.close()

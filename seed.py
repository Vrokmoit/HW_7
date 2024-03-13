from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Student, Group, Teacher, Subject, StudentMark

# Створюємо з'єднання з базою даних
engine = create_engine('postgresql://postgres:password@localhost:5432/university')

# Створюємо сесію
Session = sessionmaker(bind=engine)
session = Session()

# Ініціалізуємо Faker
fake = Faker('uk_UA')

# Генеруємо групи
groups = []
for _ in range(3):
    group = Group(name=fake.word())
    session.add(group)
    groups.append(group)

# Генеруємо викладачів
teachers = []
for _ in range(3):
    teacher = Teacher(name=fake.name())
    session.add(teacher)
    teachers.append(teacher)

# Генеруємо предмети
subjects = []
for _ in range(5, 9):
    subject = Subject(name=fake.word(), teacher=teachers[fake.random_int(0, 2)])
    session.add(subject)
    subjects.append(subject)

# Генеруємо студентів
students = []
for _ in range(30, 51):
    student = Student(name=fake.name(), group=groups[fake.random_int(0, 2)])
    session.add(student)
    students.append(student)

# Генеруємо оцінки для кожного студента по кожному предмету
for student in students:
    for subject in subjects:
        for _ in range(fake.random_int(1, 20)):
            mark = StudentMark(student=student, subject=subject, mark=fake.random_int(1, 10))
            session.add(mark)

# Зберігаємо зміни в базі даних
session.commit()

# Закриваємо сесію
session.close()

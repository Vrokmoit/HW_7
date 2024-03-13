from sqlalchemy import func, text, desc
from models import Student, Group, Teacher, Subject, StudentMark
from sqlalchemy import cast, Float

def select_1(session):
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    return session.query(Student.name, func.cast(func.avg(StudentMark.mark), Float).label('avg_grade')) \
                  .join(StudentMark).group_by(Student.id) \
                  .order_by(desc(func.cast(func.avg(StudentMark.mark), Float))).limit(5).all()


def select_2(session):
    # Знайти студента із найвищим середнім балом з предмету "кпсс"
    return session.query(Student.name, func.cast(func.avg(StudentMark.mark), Float).label('avg_grade')) \
                  .join(StudentMark).join(Subject).filter(Subject.name == 'кпсс') \
                  .group_by(Student.id).order_by(desc(func.avg(StudentMark.mark))).first()


def select_3(session):
    # Знайти середній бал у групах за певним предметом
    return session.query(func.avg(StudentMark.mark).label('average_mark'), Group.name) \
        .join(Student, Student.id == StudentMark.student_id) \
        .join(Group, Group.id == Student.group_id) \
        .join(Subject, Subject.id == StudentMark.subject_id) \
        .filter(Subject.name == 'кпсс') \
        .group_by(Group.name) \
        .all()


def select_4(session):
    # Знайти середній бал на потоці (по всій таблиці оцінок)
    avg_mark = session.query(func.avg(StudentMark.mark)).scalar()
    return round(avg_mark, 2) if avg_mark is not None else None

def select_5(session):
    # Знайти які курси читає певний викладач
    return session.query(Subject.name).join(Teacher).filter(Teacher.name == 'Антон Сич').all()

def select_6(session):
    # Знайти список студентів у певній групі
    return session.query(Student.name).join(Group).filter(Group.name == 'вечір').all()

def select_7(session):
    # Знайти оцінки студентів у окремій групі з певного предмета
    return session.query(Student.name, StudentMark.mark).join(Group).join(StudentMark).join(Subject) \
                  .filter(Group.name == "вечір", Subject.name == 'кпсс').all()

def select_8(session):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів
    return session.query(func.avg(StudentMark.mark).label('average_mark')). \
                  join(Subject).join(Teacher).filter(Teacher.name == 'Антон Сич').scalar()

def select_9(session):
    # Знайти список курсів, які відвідує певний студент
    return session.query(Subject.name).join(StudentMark).join(Student) \
                  .filter(Student.name == 'Демид Колодуб').distinct().all()

def select_10(session):
    # Список курсів, які певному студенту читає певний викладач
    return session.query(Subject.name).join(Teacher).join(StudentMark).join(Student) \
                  .filter(Student.name == 'Демид Колодуб', Teacher.name == 'Антон Сич').distinct().all()

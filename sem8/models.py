"""
Название ВУЗ-а

Информация о преподавателе
Курс
название
группа
Информация о студенте
фио
группа

Используем dictionary для создания информации о вузе
Используем list для создания информации о курсе, группе и студенте. А внутри списков реализовать dictionary
"""

university = {
    "name": "Ракетостроения",
    "address": "г.Москва, ул.Левобережная, 1 с.5"
}

courses = [
    {
        "id": 1,
        "name": "Python разработчики",
        "duration": 1
    },
    {
        "id": 2,
        "name": "C++ разработчики",
        "duration": 2
    }

]

groups = [
    {
        "id": 100,
        "name": "g100",
        "course_id": 1
    },
    {
        "id": 101,
        "name": "g101",
        "course_id": 2
    }
]

students = [
    {
        "id": 1001,
        "fio": "Ivan Petrov",
        "group_id": 100
    },
    {
        "id": 1002,
        "fio": "Petya Maximov",
        "group_id": 101
    }
]


def add_group(group):
    assert group
    # достать последнюю группу и увеличить id + 1
    group["id"] = groups[-1]["id"] + 1
    groups.append(group)


def add_student(student):
    assert student
    student["id"] = students[-1]["id"] + 1
    students.append(student)

#вывод информации о студенте по id
def find_student(id) -> dict:
    for fio in students:
        if fio["id"] == id:
            return fio
    return None

#удаление о студенте по id
def del_students(id):
    for fio in students:
        if fio["id"] == id:
            students.remove(fio)
    return


#показать студентов в группе
def find_student_in_group(group_id) -> dict:
    for fio in students:
        if fio["group_id"] == group_id:
            return fio
    return None
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
import csv
import json
from pathlib import Path

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


# вывод информации о студенте по id
def find_student(id) -> dict:
    for fio in students:
        if fio["id"] == id:
            return fio
    return None


# удаление о студенте по id
def del_students(id):
    for fio in students:
        if fio["id"] == id:
            students.remove(fio)
    return


# показать студентов в группе
def find_student_in_group(group_id) -> dict:
    for fio in students:
        if fio["group_id"] == group_id:
            return fio
    return None


def read_csv_students() -> list:
    student = []
    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            print(row)


def read_json_students() -> list:
    student = []
    with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            student.append(temp)
    return student


def write_csv_students(students: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8', newline='') as fout:
        csv_writer = csv.writer(fout)
        for student in students:
            csv_writer.writerow(student.values())


def write_json_students(students: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for student in students:
            fout.write(json.dumps(student) + '\n')


def read_csv_groups() -> list:
    group = []
    with open(Path.cwd() / 'database_gr.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            print(row)


def read_json_groups() -> list:
    group = []
    with open(Path.cwd() / 'database_gr.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            group.append(temp)
    return group


def write_csv_groups(groups: list):
    with open(Path.cwd() / 'database_gr.csv', 'w', encoding='utf-8', newline='') as fout:
        csv_writer = csv.writer(fout)
        for group in groups:
            csv_writer.writerow(group.values())


def write_json_groups(groups: list):
    with open(Path.cwd() / 'database_gr.json', 'w', encoding='utf-8') as fout:
        for group in groups:
            fout.write(json.dumps(group) + '\n')

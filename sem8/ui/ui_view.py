"""
Создаем глобальные переменные для отображения моделей
"""
from sem8.models import groups, students

MENU_UNIVERSITY_INFO = 1
MENU_GROUP_LIST = 2
MENU_ALL_STUDENTS = 3
MENU_STUDENTS_IN_GROUP = 4
MENU_ADD_GROUP = 5
MENU_ADD_STUDENT = 6
MENU_SHOW_STUDENT_BYID = 7
MENU_DEL_STUDENT = 8
MENU_EXPORT_STUDENTS_CSV = 9
MENU_EXPORT_STUDENTS_JSON = 10
MENU_IMPORT_STUDENTS_CSV = 11
MENU_IMPORT_STUDENTS_JSON = 12
MENU_EXPORT_GROUPS_CSV = 13
MENU_EXPORT_GROUPS_JSON = 14
MENU_IMPORT_GROUPS_CSV = 15
MENU_IMPORT_GROUPS_JSON = 16
MENU_EXIT = 0

MENU_ITEMS = [
    f"{MENU_UNIVERSITY_INFO}. Информация о ВУЗ",
    f"{MENU_GROUP_LIST}. Список групп",
    f"{MENU_ALL_STUDENTS}. Показать всех студентов",
    f"{MENU_STUDENTS_IN_GROUP}. Показать студентов в группе",
    f"{MENU_ADD_GROUP}. Добавить группу",
    f"{MENU_ADD_STUDENT}. Добавить студента",
    f"{MENU_SHOW_STUDENT_BYID}. Показать студента по айдишнику",
    f"{MENU_DEL_STUDENT}. Удалить студента",
    f"{MENU_EXPORT_STUDENTS_CSV}. Выгрузить всю информацию о студентах в csv-файл",
    f"{MENU_EXPORT_STUDENTS_JSON}. Выгрузить всю информацию о студентах в json-файл",
    f"{MENU_IMPORT_STUDENTS_CSV}. Загрузить всю информацию о студентах из csv-файла",
    f"{MENU_IMPORT_STUDENTS_JSON}. Загрузить всю информацию о студентах из json-файла",
    f"{MENU_EXPORT_GROUPS_CSV}. Выгрузить всю информацию о группах в csv-файл",
    f"{MENU_EXPORT_GROUPS_JSON}. Выгрузить всю информацию о группах в json-файл",
    f"{MENU_IMPORT_GROUPS_CSV}. Загрузить всю информацию о группах из csv-файла",
    f"{MENU_IMPORT_GROUPS_JSON}. Загрузить всю информацию о группах из json-файла",
    # TODO: удаление, вывод информации о студенте по id
    # TODO: выгрузить всю информацию (группы, студенты)
    # TODO: сделать загрузку информации из файла
    f"{MENU_EXIT}. Выход"
]


def print_line():
    print("-" * 30)


def show_menu():
    for item in MENU_ITEMS:
        print(item)


def show_list_item(lst):
    print_line()
    for item in lst:
        print(item)
    print_line()


def print_dict(d):
    print_line()
    print(d)
    print_line()


def show_university(university):
    print_dict(university)


def show_groups(groups):
    show_list_item(groups)


def show_group_info(group):
    print_dict(group)


def show_students_info(students):
    show_list_item(students)


def show_students_info_group(students):
    show_list_item(students)


def show_student_info(student):
    print_dict(student)


def show_id_info(id):
    print(id)


def show_fio_info(fio) -> object:
    show_list_item(fio)

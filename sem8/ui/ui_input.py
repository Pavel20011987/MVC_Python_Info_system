from .ui_view import MENU_ITEMS


def read_menu_number():
    menu_number_check = False
    menu_number = None
    while not menu_number_check:
        menu_number = input("Введите пункт меню: ")
        if not menu_number.isdigit():
            print("Введите число!", end=" ")
            continue
        menu_number = int(menu_number)
        if -1 < menu_number <= len(MENU_ITEMS):
            menu_number_check = True
        else:
            print("Такого пункта нет")

    return menu_number


def input_group():
    name = input("Название: ")
    course_id = int(input("Номер курса: "))
    return {"name": name, "course_id": course_id}


def input_student():
    fio = input("ФИО: ")
    group_id = int(input("Номер группы: "))
    return {"fio": fio, "group_id": group_id}


def get_id() -> int:
    return int(input("Введите айди студента: "))


def get_group_id() -> int:
    return int(input("Введите айди группы: "))


def get_fio() -> str:
    return input("Введите фио студента: ")


def get_student() -> dict:
    result = {}
    result["fio"] = get_fio()
    return result

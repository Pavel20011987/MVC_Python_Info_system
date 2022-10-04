from ui.ui_input import *
from ui.ui_view import *
import models

from sem8.models import del_students, students, write_csv_students, write_json_students, read_csv_students, \
    read_json_students, write_csv_groups, groups, write_json_groups, read_csv_groups, read_json_groups
from sem8.ui.ui_input import get_id, read_menu_number, get_student, get_group_id
from sem8.ui.ui_view import MENU_EXIT, MENU_STUDENTS_IN_GROUP, MENU_ALL_STUDENTS, MENU_ADD_GROUP, MENU_GROUP_LIST, \
    MENU_UNIVERSITY_INFO, show_university, MENU_SHOW_STUDENT_BYID, show_id_info, show_fio_info, show_menu, show_groups, \
    MENU_DEL_STUDENT, MENU_EXPORT_STUDENTS_CSV, MENU_EXPORT_STUDENTS_JSON, MENU_IMPORT_STUDENTS_CSV, \
    MENU_IMPORT_STUDENTS_JSON, MENU_EXPORT_GROUPS_CSV, MENU_EXPORT_GROUPS_JSON, MENU_IMPORT_GROUPS_CSV, \
    MENU_IMPORT_GROUPS_JSON


def run():
    global student
    menu_number = 1
    while menu_number != MENU_EXIT:
        show_menu()
        menu_number = read_menu_number()

        if menu_number == MENU_UNIVERSITY_INFO:
            show_university(models.university)

        elif menu_number == MENU_GROUP_LIST:
            show_groups(models.groups)

        elif menu_number == MENU_ADD_GROUP:
            group = input_group()
            models.add_group(group)
            show_group_info(group)

        elif menu_number == MENU_ALL_STUDENTS:
            show_students_info(models.students)

        elif menu_number == MENU_STUDENTS_IN_GROUP:
            group_id = get_group_id()
            fio_info_group = models.find_student_in_group(group_id)
            print(fio_info_group)

        elif menu_number == MENU_ADD_STUDENT:
            student = input_student()
            models.add_student(student)
            show_student_info(student)

        elif menu_number == MENU_SHOW_STUDENT_BYID:
            id = get_id()
            fio_info = models.find_student(id)
            print(fio_info)

        elif menu_number == MENU_DEL_STUDENT:
            id = get_id()
            fio_info = models.del_students(id)

        elif menu_number == MENU_EXPORT_STUDENTS_CSV:
            write_csv_students(students)

        elif menu_number == MENU_EXPORT_STUDENTS_JSON:
            write_json_students(students)

        elif menu_number == MENU_IMPORT_STUDENTS_CSV:
            read_csv_students()

        elif menu_number == MENU_IMPORT_STUDENTS_JSON:
            print(read_json_students())

        elif menu_number == MENU_EXPORT_GROUPS_CSV:
            write_csv_groups(groups)

        elif menu_number == MENU_EXPORT_GROUPS_JSON:
            write_json_groups(groups)

        elif menu_number == MENU_IMPORT_GROUPS_CSV:
            read_csv_groups()

        elif menu_number == MENU_IMPORT_GROUPS_JSON:
            print(read_json_groups())


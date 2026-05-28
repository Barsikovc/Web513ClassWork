from MVC_01_model import MarksModel


def check_access_role(user_role, available_roles):
    if user_role not in available_roles:
        return False
    return True


class MarksController:
    IS_SUPERUSER = 'is_superuser'
    IS_STAFF = 'is_staff'
    USER_OWNER = 'user_owner'
    GUEST = 'guest'

    def __init__(self, user_email):
        self.model = MarksModel(user_email)

    def get_default_action(self):
        return 'Добро пожаловать на главную страницу'

    def get_marks_auth(self, user_role=GUEST, available_roles=(IS_SUPERUSER, IS_STAFF, USER_OWNER)):
        access_check = check_access_role(user_role, available_roles)
        if not access_check:
            return 'Forbidden'
        if self.model.student_marks:
            return self.model.student_marks
        return None

    def get_only_courses_list(self):
        courses = []
        data = self.model.student_marks
        if data:
            for item in data:
                courses.append(item['course'])
            return courses
        return None

    def get_only_marks_list(self, user_role=GUEST, available_roles=(IS_SUPERUSER, IS_STAFF, USER_OWNER)):
        access_check = check_access_role(user_role, available_roles)
        if not access_check:
            return 'Forbidden'
        marks = []
        data = self.model.student_marks
        if data:
            for item in data:
                marks.append(item['mark'])
            return marks
        return None

    def get_all_data_list(self, user_role, available_roles=(IS_SUPERUSER, IS_STAFF, USER_OWNER)):
        access_check = check_access_role(user_role, available_roles)
        if not access_check:
            return 'Forbidden'
        return self.get_only_courses_list(), self.get_only_marks_list(user_role)

    def add_mark(self, course, mark, user_role=GUEST, available_roles=(IS_STAFF,)):
        access_check = check_access_role(user_role, available_roles)
        if not access_check:
            return 'Forbidden'
        if not isinstance(mark, int):
            return False
        if not 1 <= mark <= 12:
            return False
        self.model.add_mark(course, mark)
        return True


if __name__ == '__main__':
    student_mail = 'student1@mail.ru'
    student_controller = MarksController(student_mail)
    print(student_controller.add_mark('HTML', 10, 'is_staff'))
    print(student_controller.add_mark('CSS', 12, 'is_staff'))
    print(student_controller.add_mark('JavaScript', 9, 'is_staff'))
    print(student_controller.add_mark('JavaScript', 10, 'user_owner'))
    print(student_controller.add_mark('JavaScript', '10', 'is_staff'))
    print(student_controller.add_mark('JavaScript', 15, 'is_staff'))
    print(student_controller.get_default_action())
    print(student_controller.get_marks_auth('user_owner'))
    print(student_controller.get_only_courses_list())
    print(student_controller.get_only_marks_list('user_owner'))

import json
import termcolor
import re


class HelperMethods:

    def get_user_input(self, text, _type, limit=None):
        user_input = input(text)
        if _type == 'char':
            return self._check_character(user_input, text, _type, limit)

        if _type == 'num' and not limit:
            return self._check_number_without_limit(user_input, text, _type)

        if _type == 'num':
            return self._check_number(user_input, text, _type, limit)

    def _check_character(self, user_input, text, _type, limit):
        user_input = user_input.lower()
        is_valid = self._is_char_valid(user_input, limit)
        if not is_valid:
            print('Invalid input!')
            return self.get_user_input(text, _type, limit)
        return user_input

    def _is_char_valid(self, user_input, limit):
        if user_input in limit:
            return True
        return False

    def _check_number(self, user_input, text, _type, limit):
        validate_user_input = self._is_num_valid(user_input)
        if not validate_user_input:
            print('Invalid input!')
            return self.get_user_input(text, _type, limit)
        user_input = int(user_input)
        while True:
            if user_input <= limit and user_input >= 0:
                return user_input
            else:
                print('Invalid number input!')
                return self.get_user_input(text, _type, limit)

    def _is_num_valid(self, user_input):
        return user_input.isdigit()

    def _check_number_without_limit(self, user_input, text, _type):
        if user_input.isdigit():
            return int(user_input)
        print('Invalid input!')
        return self.get_user_input(text, _type)

    def get_data(self, path):
        try:
            with open(path, 'r')as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            return "File Not Found"

    def set_student_info(self, students_data, new_student_info, idx):
        students_data[idx] = new_student_info
        json_object = json.dumps(students_data, indent=4)
        with open('Student_info.json', 'w')as f:
            f.write(json_object)

    @staticmethod
    def escape_ansi(line):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', line)

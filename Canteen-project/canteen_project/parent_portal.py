import json


class Operations:
    def __init__():
        pass

    def recharge():
        pass

    def max_daily_credit():
        pass


class ParentPortal:
    def __init__(self):
        pass

    def _get_students_data(self):
        with open('../Student_info.json', 'r') as f:
            data = json.load(f)
        return data

    def buy_daily_meal(self):
        pass

    def not_allowed_items(self):
        pass

    def quit(self):
        pass


if __name__ == '__main__':
    # data = ParentPortal._get_students_data()
    # print(data[0])
    pass

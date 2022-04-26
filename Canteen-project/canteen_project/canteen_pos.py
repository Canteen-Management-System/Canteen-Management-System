import pandas as pd
from canteen_project.helper_methods import HelperMethods
import termcolor
from canteen_project.Store import Store
from datetime import date

PROMPTS = (
    'Enter your item: ',
    'Enter quantity: ',
    'Choose another item (C), Check out (O), back to categories (G) , Quit (Q): ',
    'Enter category Hot food (H), Snacks (S), Drinks (D), Quit (Q): ',
    'Student(T),  Not a student(N): ',
    'Enter Student ID: ',
    'Do you want to Delete (D) or Quit (Q)?: ',
    'Do you want to delete another item Y/N?: ',
    'Enter the name of the item to delete: '
)


class CanteenSystem:
    def __init__(self):
        self.hm = HelperMethods()
        self.chosen_items = {}
        self.student_data = None
        self.student_idx = None
        self.students_data = self.hm.get_data('Student_info.json')
        self.student_id = None
        self.customer_type = None

    def _reset_variables(self):
        self.chosen_items = {}
        self.student_data = None
        self.student_idx = None
        self.student_id = None
        self.customer_type = None

    @staticmethod
    def greeting():
        greet = (
            '''===================================
   Welcome to the Canteen System
===================================
              ''')
        termcolor.cprint(greet, 'green')
        return greet

    def _get_menu(self, key):
        store = Store()
        table, items = store.get_items(key)
        table_line = table.to_string(
            header=True, max_colwidth=100, index=True, index_names=False).split('\n')
        for line in table_line:
            termcolor.cprint(
                f'{line}', color='blue', attrs=['bold'])
        return items

    def _store_items(self, sub_category):
        item_idx = self.hm.get_user_input(PROMPTS[0], 'num', len(sub_category))
        item_qty = self.hm.get_user_input(PROMPTS[1], 'num')
        item = sub_category[item_idx]
        if self.student_data:
            is_allowed = self.check_not_allowed_items(
                self.student_data['Not Allowed Items'], item[0])
            if is_allowed:
                return
        try:
            if self.chosen_items[item[0]]:
                self.chosen_items[item[0]]["Quantity"] += item_qty
        except:
            self.chosen_items[item[0]] = {
                "Price": item[2], "Quantity": item_qty}

    def _get_student_id(self):
        self.student_id = int(self.hm.read_QR_code())
        print(f'Enter Student ID: {self.student_id}')

    def _id_search(self, id):
        for idx, student in enumerate(self.students_data):
            if student['id'] == id:
                self.student_data = student
                self.student_idx = idx
                return student, idx
        return None

    def _is_student_exist(self):
        self._get_student_id()
        self._id_search(self.student_id)
        if self.student_data:
            return True
        else:
            print('The ID is not exist!')
            self._is_student_exist()

    def check_not_allowed_items(self, not_allowed_items, selected_item):
        for item in not_allowed_items:
            if item == selected_item:
                print(
                    'This item not allowed for this student, Please select another item.')
                return True
        return False

    def _select_from_category(self, category):
        items = self._get_menu(category)
        self._store_items(items)

    def _get_customer_type(self):
        customer_type = self.hm.get_user_input(
            PROMPTS[4], 'char', ['t', 'n'])
        if customer_type == 't':
            self._is_student_exist()
        return customer_type

    def recipe(self):
        df = pd.DataFrame(self.chosen_items).T
        df['Amount'] = df["Price"].multiply(df["Quantity"], axis="index")
        total_row = df.sum(axis=0)
        total_row = ['', total_row[1], total_row[2]]
        df.loc[''] = ['-------', '-------', '-------']
        df.loc['Total'] = total_row
        return df, total_row[2]

    def _check_out(self, customer_type):
        if customer_type == 't':
            self.credit_payment()
        if customer_type == 'n':
            self.cash_payment()

    def cash_payment(self):
        df, total = self.recipe()
        self._print_table(df, 'red', ['bold'])
        cash = self.hm.get_user_input('Cash amount : ', 'float', total)
        change = cash - total
        df.loc['Cash'] = ['', '', cash]
        df.loc['Change'] = ['', '', change]
        self._print_table(df, 'red', ['bold'])
        self.meal_quantity()

    def _print_table(self, df, _color, _attrs=[]):
        table_line = df.to_string(
            header=True, index=True, index_names=True).split('\n')
        for line in table_line:
            termcolor.cprint(line, color=_color,
                             attrs=_attrs)

    def credit_payment(self):
        if len(self.chosen_items) == 0:
            print("Please place your order before continiou...")
            return self.logic()
        df, total = self.recipe()
        self._print_table(df, 'red', ['bold'])
        credit_balance = self.student_data['Balance']
        max_daily_credit = self.student_data['Max Daily Credit']
        if total <= max_daily_credit and total < credit_balance:
            new_balance = credit_balance - total
            self.student_data['Balance'] = new_balance
            df.loc['Av. Balance:'] = ['', '', credit_balance]
            df.loc['New Balance:'] = ['', '', new_balance]
            self.hm.set_student_info(
                self.students_data, self.student_data, self.student_idx)
            self._print_table(df, 'red', ['bold'])
            self.meal_quantity()
            self.student_daily_order()
        else:
            termcolor.cprint(
                text="The total exceed the max daily credit or your balance is not enough!",
                color='red', attrs=['bold', 'underline']
            )
            user_input = self.hm.get_user_input(
                PROMPTS[6], 'char', ['d', 's', 'q'])
            if user_input == 'd':
                self.delete_item()
            if user_input == 's':
                self.cash_payment()

    def _is_cart_empty(self):
        return len(self.chosen_items) == 0

    def delete_item(self):
        def _delete_again():
            while True:
                delete_again = self.hm.get_user_input(
                    PROMPTS[7], 'char', ['n', 'y'])
                if delete_again == 'y':
                    return self.delete_item()
                elif delete_again == 'n':
                    return self.credit_payment()
        cart_keys = [i.lower() for i in list(self.chosen_items.keys())]
        user_input = self.hm.get_user_input(
            PROMPTS[8], 'char', cart_keys).capitalize()
        quantity = self.chosen_items[user_input]['Quantity']
        get_qty = self.hm.get_user_input(
            f'You have {quantity} items of {user_input}, how many item/s you want to delete: ',
            'num',
            quantity
        )
        self.chosen_items[user_input]['Quantity'] -= get_qty
        if self.chosen_items[user_input]['Quantity'] == 0:
            self.chosen_items.pop(user_input)
        if self._is_cart_empty():
            termcolor.cprint("\nYour cart are empty!\n", 'red')
            return self.logic()
        return _delete_again()

    def _quiting(self):
        termcolor.cprint("""
===============================================================
Thank you for visiting
===============================================================
""", 'green')

    def logic(self):
        if not self.customer_type:
            self.customer_type = self._get_customer_type()
        get_user_category = self.hm.get_user_input(
            PROMPTS[3], 'char', ['s', 'h', 'q', 'd'])

        def _categories(category):
            if category == 's':
                self._select_from_category('Snacks')
            if category == 'h':
                self._select_from_category('Hot food')
            if category == 'd':
                self._select_from_category('Drinks')

        user_action = get_user_category
        while True:
            if user_action in ['s', 'h', 'd']:
                get_user_category = user_action
                _categories(get_user_category)
                user_action = self.hm.get_user_input(
                    PROMPTS[2], 'char', ['c', 'o', 'g', 'q'])
                continue

            if user_action == 'c':
                _categories(get_user_category)
                user_action = self.hm.get_user_input(
                    PROMPTS[2], 'char', ['c', 'o', 'g', 'q'])
                continue

            if user_action == 'g':
                user_action = self.hm.get_user_input(
                    PROMPTS[3], 'char', ['s', 'h', 'q', 'd'])
                continue

            if user_action == 'o':
                self._check_out(self.customer_type)
                # self._quiting()
                # self._reset_variables()
                # return self.logic()
                break

            if user_action == 'q':
                self._quiting()
                break

    def student_daily_order(self):
        data = self.hm.get_csv('studentDailyOrder.csv')
        df, total = self.recipe()
        new_data = [self.student_data['id'],
                    self.student_data['name'], date.today(), total]
        data.append(new_data)
        self.hm.set_csv('studentDailyOrder.csv', data)

    def meal_quantity(self):
        data = self.hm.get_csv('MealQuantity.csv')
        recipe = list(self.chosen_items.items())
        for i in recipe:
            list1 = [i[0], date.today(), i[1]['Quantity']]
            data.append(list1)
        self.hm.set_csv('MealQuantity.csv', data)


if __name__ == '__main__':
    from Store import Store
    CanteenSystem.greeting()
    canteen = CanteenSystem()
    canteen.logic()

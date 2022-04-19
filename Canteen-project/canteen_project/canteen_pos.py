
class CanteenSystem:

    def __init__(self):
        pass

    @ staticmethod
    def greeting():
        greet = (
            '''===================================
   Welcome to the Canteen System
===================================
              ''')
        print(greet)
        return greet

    def menu(self, key):
        store = Store()
        table, items = store.get_items(key)
        return table, items

    def order(self):
        user_input = input(
            'Enter category Hot food (H), Snacks (S), Drinks (d), Quit (Q): ')
        while user_input.lower() != 'q':
            if user_input.lower() == 'h':
                table, items = self.menu('Hot food')
                print(table)
                pass
            if user_input.lower() == 's':
                table, items = self.menu('Snacks')
                print(table)

            if user_input.lower() == 'd':
                table, items = self.menu('Drinks')
                print(table)

    def recipe(self):
        pass


if __name__ == '__main__':
    from Store import Store
    CanteenSystem.greeting()

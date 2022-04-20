
class CanteenSystem:

    def __init__(self):
        self.chosen_items = {}

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

    def _chosen_item(self, sub_category):
        TEXT_ITEM_IDX = 'Enter your item: '
        TEXT_ITEM_QTY = 'Enter quantity: '
        TEXT = 'Choose another item (C), Check out (O), back to categories (G) , Quit (Q): '

        def _store_items():
            item_idx = int(input(TEXT_ITEM_IDX))
            while item_idx > len(sub_category)-1 or item_idx < 0:
                item_idx = input(TEXT_ITEM_IDX)
            item_qty = int(input(TEXT_ITEM_QTY))
            sub_category[item_idx][0]

        _store_items()
        user_input = input(TEXT)
        while True:
            if user_input.lower() == 'q':
                break
            _store_items()
            user_input = input(TEXT)
        return user_input

    def order(self):
        TEXT = 'Enter category Hot food (H), Snacks (S), Drinks (d), Quit (Q): '
        user_input = input(TEXT)
        while user_input.lower() != 'q':
            if user_input.lower() == 'h':
                table, items = self.menu('Hot food')
                print(table)
                user_input = self._chosen_item(items)

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
    canteen = CanteenSystem()
    canteen.order()

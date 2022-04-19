import pandas as pd
class CanteenSystem:

    def __init__(self):
        self.chosen_items = {}
        self.cash =  False
        

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
         
            item = sub_category[item_idx]
            try:
                if self.chosen_items[item[0]]:
                    
                    self.chosen_items[item[0]]["quantity"]+=item_qty
                    
            except:
                self.chosen_items[item[0]]={"price":item[2], "quantity":item_qty}
            print (self.chosen_items)
        _store_items()
        user_input = input(TEXT)
        while True:
            if user_input.lower() == 'q':
                return user_input
            if user_input.lower() == 'g':
                return user_input
            if user_input.lower() == 'o':
                return user_input
            _store_items()
            user_input = input(TEXT)
        

    def order(self):
        TEXT = 'Enter category Hot food (H), Snacks (S), Drinks (d), Quit (Q): '
        user_input = input(TEXT)
        while True:
            if user_input.lower() == 'q':
                    print( """
===============================================================
Thank you for visiting
===============================================================
""")
                    break
            if user_input.lower() == 'h':
                table, items = self.menu('Hot food')
                print(table)
                user_input = self._chosen_item(items)

            if user_input.lower() == 's':
                table, items = self.menu('Snacks')
                print(table)
                user_input = self._chosen_item(items)
            if user_input.lower() == 'd':
                table, items = self.menu('Drinks')
                print(table)
                user_input = self._chosen_item(items)
            if user_input.lower() == 'g':
               return self.order()
            if user_input.lower() == 'o':
                payment_method=input('Payment method: Credit (R), Cash (S): ').lower()
                self.payment_method(payment_method)
                return 
                

    def recipe(self):
        df = pd.DataFrame(self.chosen_items).T
        df['total']= df["price"].multiply(df["quantity"], axis="index")
        sum_column = df.sum(axis=0)
        sum_column = ['',sum_column[1],sum_column[2]]
        df.loc[''] =['-------', '------' , '-------']

        df.loc['Total'] = sum_column
        return df,sum_column[2]
        
    def payment_method(self,method):
        if method == 's':
            return self.cash_payment()
        elif method == 'r':
            return self.credit_payment()
        
    def cash_payment(self):
        df,total = self.recipe()
        print(df)
        print('')
        cash= float(input('Cash amount : '))
        change = cash - total
        df.loc['Cash'] =['', '' , cash]
        df.loc['Change']=['','', change]
        print(df)
        
    def credit_payment(self):
        pass

if __name__ == '__main__':
    from Store import Store
    CanteenSystem.greeting()
    canteen = CanteenSystem()
    canteen.order()
    
    

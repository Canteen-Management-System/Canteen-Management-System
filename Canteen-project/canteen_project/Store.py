import csv
from itertools import count
import pandas as pd
import json
from canteen_project.queue import Queue,Node
import termcolor
from csv import writer




class Store():
    def __init__(self):
        self.menu = "menu"
        self.queue1 = Queue()

    def _get_menu_data(self):
        with open('menu.json', 'r') as f:
            menu = json.load(f)
        return menu

    def get_items(self, key):
        items = self._get_menu_data()
        indics = [i for i in range(len(items[key]))]
        table = pd.DataFrame(items[key], indics, items['headers'])
        return table, items[key]
    
    def Add_item(self):
        pass

    def online_order(self, stdid, meal, date):
        self.queue1.enqueue(stdid)
        self.queue1.enqueue(meal)
        self.queue1.enqueue(date)


    def pop_online_orders(self):
            with open('foodorders.csv') as file_obj:
                # Skips the heading
                # Using next() method
                # heading = next(file_obj)
                
                # Create reader object by passing the file 
                # object to reader method
                reader_obj = csv.reader(file_obj)
                
                # Iterate over each row in the csv file 
                # using reader object
                print( "\n you have the below Online orders : \n " )
                count = 1
                for row in reader_obj:
                    print(f'{count} : {str(row)}')
                    count+=1
            if count == 1:
                print("\n \n there are no pending orders .. ")
            deliver = input ("Type Yes (Y) to deliver the first order , No (N) to Quit and deliver later ")
            if deliver.lower() == "y":
                url = "foodorders.csv"
                df = pd.read_csv(url)
                df = df.iloc[1:]
                df.to_csv('foodorders.csv',                              # Export pandas DataFrame
                sep = ",")

                print("Thank you ")
        
                        





        

    def store_portal(self):
        print( termcolor.colored('''
        ****************************************************************
        ************  Welcome to Canteen Store Portal *****************
        ****************************************************************
        ''' , "green" ))
        while(True):
            task = input(termcolor.colored ('''
                Type In the letter between parentheses to select the option .. \n
                Add Items (A),
                view Available Item (V),
                online orders (O),
                Quit (Q):  >>  ''', "red"))
            if task.lower() == "q":
                print(termcolor.colored("\n Thank you for using Canteen- Store System \n","red"))
                break
            elif task.lower() == "a":
                self.Add_item()
            elif task.lower() == "v":
                while (True):
                    Category = input(termcolor.colored ('Enter category Hot food (H), Snacks (S), Drinks (d), Quit  (Q) >>   ', "magenta" ))
                    if Category.lower() == 'h':
                        table, items = self.get_items('Hot food')
                        print(table)
                    elif Category.lower() == 's':
                        table, items = self.get_items('Snacks')
                        print(table)
                    elif Category.lower() == 'd':
                        table, items =self.get_items('Drinks')
                        print(table)
                    elif Category.lower() == "q":
                        break
            elif task.lower() == "o":
                self.pop_online_orders()
            else:
                continue


if __name__ == '__main__':
    store1 = Store()
    store1.store_portal()



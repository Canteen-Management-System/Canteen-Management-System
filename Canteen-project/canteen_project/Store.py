import csv
from itertools import count
from re import A
from tkinter import Menu
import pandas as pd
import json

from sqlalchemy import true
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
        menu = self._get_menu_data()
        while true:
            key = ""
            add = []
            Category = input(termcolor.colored ('Enter category Hot food (H), Snacks (S), Drinks (d), Quit  (Q) >>   ', "magenta" ))
            if Category.lower() == 'h':
                key = "Hot food"
            elif Category.lower() == 's':
                key = 'Snacks'
            elif Category.lower() == 'd':
                key = 'Drinks'
            elif Category.lower() == "q":
                        break
            mname  = input("Meal Name  >> ")
            add.append(mname)
            mdescribtion = input (" Description  >>")
            add.append(mdescribtion)
            mprice = input("price   >> ")
            add.append(mprice)
            menu[key] += [add]
            f = open("menu.json", "w")
            json.dump(menu, f)
            f.close()
        print("\n\n Items added ..")


    def pop_online_orders(self):
            listofRows = []
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
                    print(f'{count}  : StID = {row[0]}   Date = {row[1]}    Meal no. {row[2]}')
                    listofRows.append(row)
                    count+=1
            if count == 1:
                print(termcolor.colored("\n \n there are no pending orders ..\n ","yellow"))
            deliver = input ("Type Yes (Y) to deliver the first order , No (N) to Quit and deliver later ")
            if deliver.lower() == "y":
            # writing to csv file 
                with open('foodorders.csv', 'w') as csvfile: 
                    # creating a csv writer object 
                    csvwriter = csv.writer(csvfile) 
                    # writing the data rows 
                    i = 1
                    for i in range(len(listofRows)-1):
                        csvwriter.writerow(listofRows[i+1])
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



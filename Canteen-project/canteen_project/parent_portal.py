import json
from textwrap import indent
import pandas as pd
import datetime
from datetime import date
import calendar
import termcolor
import os
from csv import writer
import matplotlib.pyplot as plt
from IPython.display import display, Image
from mdutils.mdutils import MdUtils
import numpy as np  # linear algebra
import pandas as pd


os.system('color')


class Operations():
    '''
    Class Operation with Two methods to perform the Basic Operation related to the Balance 
    1- Recharge 
    2- Max deaily Credit .
    '''

    def __init__(self):
        pass

    def recharge(stdId, RechAmount):
        '''
        Recharge method : add certain amount to the Balance
        input : student ID , Recharge Amount 
        output : the updated students infromation with new Balance  
        '''
        P1 = ParentPortal()
        AllstdInfo = P1._get_students_data()
        for p in AllstdInfo:
            if p['id'] == int(stdId):
                p["Balance"] += float(RechAmount)
        # Serializing json
        json_object = json.dumps(AllstdInfo, indent=4)

        # Writing to sample.json
        with open('Student_info.json', "w") as outfile:
            outfile.write(json_object)

        def search(id):
            for p in AllstdInfo:
                if p['id'] == int(stdId):
                    return p
        data = search(stdId)
        P1.print_std_info(data)
        return data

    def max_daily_credit(stdid, maxCred):
        '''
        Set the Maximum daily allowed credit which can be used by a students for any day 
        input : student ID , maimum Credit  Amount 
        output : the updated students infromation with new max credit amount  
        '''
        P1 = ParentPortal()
        AllstdInfo = P1._get_students_data()
        for p in AllstdInfo:
            if p['id'] == int(stdid):
                p["Max Daily Credit"] = float(maxCred)
        # Serializing json
        json_object = json.dumps(AllstdInfo, indent=4)

        # Writing to sample.json
        with open('Student_info.json', "w") as outfile:
            outfile.write(json_object)

        def search(id):
            for p in AllstdInfo:
                if p['id'] == int(stdid):
                    return p
        data = search(stdid)
        P1.print_std_info(data)
        return data


class ParentPortal:
    '''
    class Prent Portal which will be used by parent to fully mange the student in the Canteen mangment system 
    methods : 
    1- get students data 
    2- Canteen Portal .
    3- buy daily meal for online dailvery from the kitchen 
    4- Not allowed items that the student cant buy from the Canteen .
    '''

    def __init__(self):
        pass

    def _get_students_data(self):
        '''
        method :  get studnt data 
        input : path of the Jeson file  
        output : read and return the whole file data 
        '''
        with open('Student_info.json', 'r') as f:
            data = json.load(f)
        return data

    def canteen_portal(self):
        '''
        main methods in the class which used to connect all methods required to 
        operate the portal and give the parent full control .
        no argument , not returning any data , only perform Operation .
        '''
        print(termcolor.colored('''
        ****************************************************************
        ************  Welcome to Canteen Parent Portal *****************
        ****************************************************************
        ''', "yellow"))
        stdId = input(termcolor.colored(
            " Enter the Student ID:  >>   ", "magenta"))
        AllstdInfo = self._get_students_data()

        def search(id):
            for p in AllstdInfo:
                if p['id'] == int(stdId):
                    return p
        data = search(stdId)
        self.print_std_info(data)
        while(True):
            oper = input(termcolor.colored('''
            Type In the letter between parentheses to select the option .. \n
            Recharge (R),
            Set_Max-Daily-Credit (M),
            Not-Allowed Items (N),
            Buy daily meal (B),
            Reports and Analysis (A)
            Foods word anlysis (F)
            Quit (Q):  >>  ''', "magenta"))
            if oper.lower() == "q":
                print(termcolor.colored(
                    "\n Thank you for using Canteen System , We Care ! \n", "magenta"))
                break
            elif oper.lower() == "r":
                RechAmount = input(termcolor.colored(
                    "Enter amount of charge:   >> ", "magenta"))
                Operations.recharge(stdId, RechAmount)
            elif oper.lower() == "m":
                maxCred = input(termcolor.colored(
                    "Enter the daily balance:  >> ", "magenta"))
                Operations.max_daily_credit(stdId, maxCred)
            elif oper.lower() == "n":
                self.not_allowed_items(stdId)
            elif oper.lower() == "b":
                self.buy_daily_meal(stdId)
            elif oper.lower() == "a":
                self.Std_Report(stdId)
            elif oper.lower() == "f":
                self.data_analysis()
            else:
                continue

    def Std_Report(self, stdId):
        Report = input(termcolor.colored("\n Select Report Number: "
                                         "\n1- student Daily purchese Report ."
                                         "\n2- Item purchese Qunaity , which show the Top item purchese in the Canteen  ", "magenta"))
        if (Report == "2"):
            x = []
            y = []

            with open('MealQuantity.csv', 'r') as csvfile:
                plots1 = writer.reader(csvfile, delimiter=',')

                for row in plots1:
                    x.append(row[0])
                    y.append(row[2])

            plt.bar(x, y, color='g', width=0.72, label="IdVSItem")
            plt.xlabel('Item')
            plt.ylabel('Quantity')
            plt.title('Items Quantity')
            plt.legend()
            plt.plot(x, y)

            plt.show(block=True)
            plt.savefig('Report2.png')

        elif (Report == "1"):
            Xx = []
            Yy = []

            with open('studentDailyOrder.csv', 'r') as csvfile:
                plots2 = writer.reader(csvfile, delimiter=',')

                for row in plots2:
                    if row[0] == stdId:
                        Xx.append(row[2])
                        Yy.append(row[3])

            plt.bar(Xx, Yy, color='g', width=0.72, label="food")
            plt.xlabel('Date')
            plt.ylabel('amount')
            plt.title('purchese amount for an interval ')
            plt.legend()
            plt.plot(Xx, Yy)

            plt.show(block=True)
            plt.savefig('Report1.png')

    def data_analysis(self):
        Xlist = []
        ylist = []

        with open('canteen_project/nutrients_csvfile.csv', 'r') as csvfile:
            plots = writer.reader(csvfile, delimiter=',')

            for row in plots:
                Xlist.append(row[0])
                ylist.append(row[3])

        plt.bar(Xlist, ylist, color='g', width=0.72, label="food")
        plt.xlabel('Food')
        plt.ylabel('Calories')
        plt.title('Calories for diff food ')
        # plt.legend()
        # plt.plot(Xlist, ylist)

        # plt.show(block=True)
        plt.savefig('FoodVSCalories.png')

        # #####################********************************8############################
        W = []
        Z = []
        with open('canteen_project/nutrients_csvfile.csv', 'r') as csvfile:
            plots = writer.reader(csvfile, delimiter=',')
            for row in plots:
                W.append(row[0])
                Z.append(row[4])

        plt.plot(W, Z, color='g', linestyle='dashed',
                 marker='o', label="Protein")

        plt.xticks(rotation=25)
        plt.xlabel('Food')
        plt.ylabel('Protein')
        plt.title('Protein for diff food', fontsize=20)
        plt.grid()
        # plt.legend()
        # plt.show()
        plt.savefig('FoodVSProtein.png')
        # img = mpimg.imread('FoodVSProtein.png')
        # imgplot = plt.imshow(img)
        # plt.show()
        self.md_file_analysis()

        # 3

    def md_file_analysis(self):
        '''
        method used to organized the data analysis and visulaization of the Reports 
        '''
        mdFile = MdUtils(file_name='foodAnalysis',
                         title='Nutritional Facts for most common foods')

        # style is set 'atx' format by default.
        mdFile.new_header(level=1, title='Overview')

        mdFile.new_paragraph("Everybody nowadays is mindful of what they eat."
                             "Counting calories and reducing fat intake is the number one advice given by all dieticians and nutritionists."
                             "Therefore, we need to know what foods are rich in what nutrients, don't we?")
        mdFile.new_paragraph()
        mdFile.new_header(level=2, title="Content")
        mdFile.new_paragraph("this  analysis contains a data for the Top 20 foods in the world each with the amount of Calories,"
                             "Fats, Proteins, Saturated Fats, Carbohydrates, Fibers labelled for each food. "
                             "Also, the foods are also categorised into various groups like Desserts, Vegetables, Fruits etc.")

        # ********************************************************************************************************************
        # ******************************************** Paragraph and Text format *********************************************
        # ********************************************************************************************************************
        mdFile.new_header(level=2, title="Top 20 Food Vs Calories")
        mdFile.new_paragraph(
            " check out this graphs show  the comparison  of the Calories for each of the food lidt ")

        image_text = "FoodVSCalories"
        path = "FoodVSCalories.png"
        mdFile.new_line(mdFile.new_inline_image(text=image_text, path=path))

        mdFile.new_header(level=2, title="Top 20 Food Vs Protein")
        mdFile.new_paragraph(
            " check out this graphs show  the comparison  of the Protein for each of the food lidt ")

        image_text = "FoodVSProtein"
        path = "FoodVSProtein.png"
        mdFile.new_line(mdFile.new_inline_image(text=image_text, path=path))

        mdFile.write('\n')
        # Create a table of contents
        mdFile.new_table_of_contents(table_title='Contents', depth=2)
        mdFile.create_md_file()

    def buy_daily_meal(self, stdId):
        '''
        Buy Daily Meal method used to perform the online purchese from parent 
        the price will be deduct from the Balance direct , the parent can order the meal 
        one day inadvance , the meal name , studentID , and the date will be sent to the 
        school kitchen to prepare the meal .
        input : student ID 
        '''
        store = Store()
        today = datetime.date.today()
        curr_date = date.today()
        index = curr_date.weekday()
        index2 = index + 1
        if index == 6:
            index2 = 0

        day = calendar.day_name[index2]
        mealdate = today + datetime.timedelta(days=1)
        if day == "Friday":
            day = "Sunday"
            mealdate = mealdate + datetime.timedelta(days=1)
            mealdate = mealdate + datetime.timedelta(days=1)
        if day == "Saturday":
            day = "Sunday"
            mealdate = mealdate + datetime.timedelta(days=1)
        print(" Choose your student daily meal  >> ")
        print(f'* Available meals for the next Day  {mealdate} {day}   >>')
        table, items = store.get_items('Hot food')
        print(table)
        meal = input(termcolor.colored("Select meal:  >> ", "magenta"))
        print(
            f'Student will receive {items[int(meal)][1]} on {day} {mealdate} ')
        price = items[int(meal)][2] * -1
        print(f' {items[int(meal)][2]} JD will be detacted from his Balance ')
        Operations.recharge(stdId, price)
        ###################################################

        # data rows of csv file
        rows = [stdId, mealdate, meal]

        # name of csv file
        filename = "foodorders.csv"

        # writing to csv file
        with open('foodorders.csv', 'a', newline='') as f_object:
            # Pass the CSV  file object to the writer() function
            writer_object = writer(f_object)
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerow(rows)
            # Close the file object
            f_object.close()
        AllstdInfo = self._get_students_data()
        meadapp = []
        meadapp.append(items[int(meal)][1])
        meadapp.append(str(mealdate))
        for p in AllstdInfo:
            if p['id'] == int(stdId):
                p["Daily meal"].append(meadapp)
        # Serializing json
        json_object = json.dumps(AllstdInfo, indent=4)

        # Writing to sample.json
        with open('Student_info.json', "w") as outfile:
            outfile.write(json_object)
        return stdId, meal, mealdate

    def not_allowed_items(self, stdId):
        '''
        methods used to help the parent select list of not allowed items to be added to the student account 
        input : student ID 
        output : list of the name of not allowed meals 
        '''
        C1 = CanteenSystem()
        store = Store()
        print(termcolor.colored('''
        Select the Category then you will see the list of the Available items
        select which items you will Not allow the student to buy from Canteen
        ''', "magenta"))
        NotAllowedList = []
        AllstdInfo = self._get_students_data()
        while (True):
            Category = input(termcolor.colored(
                'Enter category Hot food (H), Snacks (S), Drinks (d), Quit  (Q) >>   ', "magenta"))
            if Category.lower() == 'h':
                table, items = store.get_items('Hot food')
                print(table)
            elif Category.lower() == 's':
                table, items = store.get_items('Snacks')
                print(table)
            elif Category.lower() == 'd':
                table, items = store.get_items('Drinks')
                print(table)
            elif Category.lower() == "q":

                if len(NotAllowedList) != 0:
                    print(termcolor.colored('''
                 you have Selected the below list as Not allowed to buy from Canteen  >>> 
                ''', "magenta"))
                    for i in range(len(NotAllowedList)):
                        print(f'{i+1} - {NotAllowedList[i]}')
                    break
            else:
                continue
            NotallowedItem = input(termcolor.colored(
                "Enter item by number  >>  ", "magenta"))
            NotAllowedList.append(items[int(NotallowedItem)][0])
            for p in AllstdInfo:
                if p['id'] == int(stdId):
                    p["Not Allowed Items"].append(
                        items[int(NotallowedItem)][0])
        # Serializing json
        json_object = json.dumps(AllstdInfo, indent=4)

        # Writing to sample.json
        with open('Student_info.json', "w") as outfile:
            outfile.write(json_object)
        return NotAllowedList

    def print_std_info(self, data):
        '''
        print function used to print the basic student information 
        '''
        print(f'''
        Student Info
        _________________
        ID              : {data["id"]}
        Name            : {data["name"]}
        Balance         : {data["Balance"]} JOD
        Max daily credit: {data["Max Daily Credit"]} JOD
        ''')


if __name__ == '__main__':
    from canteen_pos import CanteenSystem
    from Store import Store
    parent1 = ParentPortal()
    parent1.canteen_portal()

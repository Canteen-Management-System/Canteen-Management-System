import json
from textwrap import indent
import pandas as pd
import datetime
from datetime import date
import calendar
import termcolor
import os
from csv import writer
from IPython.display import display, Image
from mdutils.mdutils import MdUtils
import pandas as pd
import subprocess




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


    def Std_Report(self,stdId):
        print(termcolor.colored( " Kindly Open the below link by click on both Ctr + click on the link to get \n student Daily purchese Report .","magenta") )
        process = subprocess.Popen(["streamlit", "run", os.path.join(
        'Analysis', 'stdAnalysis.py')])
        

    def data_analysis(self):
        process = subprocess.Popen(["streamlit", "run", os.path.join(
        'Analysis', 'analysisFood.py')])
       
        
    def buy_daily_meal(self,stdId):
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

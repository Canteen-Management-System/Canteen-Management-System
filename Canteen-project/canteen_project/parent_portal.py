import json
import pandas as pd
from canteen_project.canteen_pos import CanteenSystem
from canteen_project.Store import Store
import datetime 
from datetime import date
import calendar
import termcolor
import os
os.system('color')

class Operations():
    '''
    Class Operation with Two methods to perform the Basic Operation related to the Balance 
    1- Recharge 
    2- Max deaily Credit .
    '''
    def __init__(self):
        pass

    def recharge(stdId,RechAmount):
        '''
        Recharge method : add certain amount to the Balance
        input : student ID , Recharge Amount 
        output : the updated students infromation with new Balance  
        '''
        P1= ParentPortal()
        AllstdInfo = P1._get_students_data()
        for p in AllstdInfo:
            if p['id'] == int(stdId):
                p["Balance"] += float(RechAmount)
        # Serializing json 
        json_object = json.dumps(AllstdInfo, indent = 4)
  
        # Writing to sample.json
        with open('/home/student88/CanteenMangmentSystem/Canteen-Management-System/Canteen-project/Student_info.json', "w") as outfile:
            outfile.write(json_object)
        def search(id):
            for p in AllstdInfo:
                if p['id'] == int(stdId):
                    return p
        data = search(stdId)
        P1.print_std_info(data)
        return data


    def max_daily_credit(stdid , maxCred):
        '''
        Set the Maximum daily allowed credit which can be used by a students for any day 
        input : student ID , maimum Credit  Amount 
        output : the updated students infromation with new max credit amount  
        '''
        P1= ParentPortal()
        AllstdInfo = P1._get_students_data()
        for p in AllstdInfo:
            if p['id'] == int(stdid):
                p["Max Daily Credit"] = float(maxCred)
        # Serializing json 
        json_object = json.dumps(AllstdInfo, indent = 4)
  
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
        print( termcolor.colored('''
        ****************************************************************
        ************  Welcome to Canteen Parent Portal *****************
        ****************************************************************
        ''' , "yellow" ))
        stdId = input(" Enter the Student ID:  ")
        AllstdInfo = self._get_students_data()
        def search(id):
            for p in AllstdInfo:
                if p['id'] == int(stdId):
                    return p
        data = search(stdId)
        self.print_std_info(data)
        while(True):
            oper = input("Recharge (R), Set_Max-Daily-Credit (M), Not-Allowed Items (N), Buy daily meal (B), Quit (Q):")
            if oper.lower() == "q":
                break
            elif oper.lower() == "r":
                RechAmount = input("Enter amount of charge: ")
                Operations.recharge(stdId,RechAmount)
            elif oper.lower() == "m":
                maxCred = input("Enter the daily balance: ")
                Operations.max_daily_credit(stdId , maxCred )
            elif oper.lower() == "n":
                self.not_allowed_items(stdId)
            elif oper.lower() == "b":
                self.buy_daily_meal(stdId)
            else:
                continue


        
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
        day = calendar.day_name[curr_date.weekday()+1]
        mealdate = today + datetime.timedelta(days = 1) 
        if day == "Friday" :
            day = "Sunday"
            mealdate = mealdate + datetime.timedelta(days = 1) 
            mealdate = mealdate + datetime.timedelta(days = 1)
        if day == "Saturday": 
            day = "Sunday"
            mealdate = mealdate + datetime.timedelta(days = 1) 
        print(" Choose your student daily meal  >> ")
        print (f'* Available meals for the next Day  {mealdate} {day}   >>')
        table, items = store.get_items('Hot food')
        print(table)
        meal = input ("Select meal:  >> ")
        print(f'Student will receive {items[int(meal)][1]} on {day} {mealdate} ')
        price = items[int(meal)][2] * -1
        print(f' {items[int(meal)][2]} JD will be detacted from his Balance ')
        Operations.recharge(stdId, price)
        store.online_order(stdId , meal , mealdate )
        AllstdInfo = self._get_students_data()
        meadapp = []
        meadapp.append(items[int(meal)][1])
        meadapp.append(str(mealdate))
        for p in AllstdInfo:
            if p['id'] == int(stdId):
                    p["Daily meal"].append(meadapp)
        # Serializing json 
        json_object = json.dumps(AllstdInfo, indent = 4)
    
        # Writing to sample.json
        with open('Student_info.json', "w") as outfile:
            outfile.write(json_object)
        return stdId , meal , mealdate


    def not_allowed_items(self,stdId):
        '''
        methods used to help the parent select list of not allowed items to be added to the student account 
        input : student ID 
        output : list of the name of not allowed meals 
        '''
        C1 = CanteenSystem()
        store = Store()
        print('''
            
            **  Choose the Not allowed list of Items  **

        ''')
        NotAllowedList = []
        AllstdInfo = self._get_students_data()
        while (True):
            Category = input('Enter category Hot food (H), Snacks (S), Drinks (d), Quit  (Q)   ' )
            if Category.lower() == 'h':
                table, items = store.get_items('Hot food')
                print(table)
            if Category.lower() == 's':
                table, items = store.get_items('Snacks')
                print(table)
            if Category.lower() == 'd':
                table, items =store.get_items('Drinks')
                print(table)
            if Category.lower() == "q":
                
                if len(NotAllowedList) != 0 :
                    print('''
                 you have Selected the below list as Not allowed to buy from Canteen  >>> 
                ''')
                    for i in range (len(NotAllowedList)):
                        print (f'{i+1} - {NotAllowedList[i]}')
                    break
            NotallowedItem = input ("Enter item by number  >  ")
            NotAllowedList.append(items[int(NotallowedItem)][0])
            for p in AllstdInfo:
                if p['id'] == int(stdId):
                    p["Not Allowed Items"].append(items[int(NotallowedItem)][0])
        # Serializing json 
        json_object = json.dumps(AllstdInfo, indent = 4)
    
        # Writing to sample.json
        with open('Student_info.json', "w") as outfile:
            outfile.write(json_object)
        return NotAllowedList

            


    def print_std_info(self,data):
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
    parent1 = ParentPortal()
    parent1.canteen_portal()

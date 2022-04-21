import json
import pandas as pd
from canteen_project.canteen_pos import CanteenSystem
from canteen_project.Store import Store
import datetime 
from datetime import date
import calendar





class Operations():
    def __init__(self):
        pass

    def recharge(stdId,RechAmount):
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
    def __init__(self):
        pass
    def _get_students_data(self):
        with open('Student_info.json', 'r') as f:
            data = json.load(f)
        return data

    def canteen_portal(self):
        print('''

        ************  Welcome to Canteen Parent Portal *****************
        
        ''')
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
            if oper == "Q":
                break
            elif oper == "R":
                RechAmount = input("Enter amount of charge: ")
                Operations.recharge(stdId,RechAmount)
            elif oper == "M":
                maxCred = input("Enter the daily balance: ")
                Operations.max_daily_credit(stdId , maxCred )
            elif oper == "N":
                self.not_allowed_items(stdId)
            elif oper == "B":
                self.buy_daily_meal(stdId)
            else:
                continue


        
    def buy_daily_meal(self,stdId):
        store = Store()
        today = datetime.date.today()
        curr_date = date.today()
        day = calendar.day_name[curr_date.weekday()+1]
        tomorrow = today + datetime.timedelta(days = 1) 
        if day == "Friday" :
            day = "Sunday"
            tomorrow = tomorrow + datetime.timedelta(days = 1) 
            tomorrow = tomorrow + datetime.timedelta(days = 1)
        if day == "Satarday": 
            day = "Sunday"
            tomorrow = tomorrow + datetime.timedelta(days = 1) 
        print(" Choose your student daily meal  >> ")
        print (f'* Available meals for tomorrow  {tomorrow} {day}   >>')
        table, items = store.get_items('Hot food')
        print(table)
        meal = input ("Select meal:  >> ")
        print(f'Student will receive {items[int(meal)][1]} on {day} {tomorrow} ')
        price = items[int(meal)][2] * -1
        print(f' {items[int(meal)][2]} will be detacted from his Balance ')
        Operations.recharge(stdId, price)


    def not_allowed_items(self,stdId):
        C1 = CanteenSystem()
        store = Store()
        print('''
            
            **  Choose the Not allowed list of Items  **

        ''')
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
            if Category == "Q":
                print('''
                 you have Selected the below list as Not allowed to buy from Canteen  >>> 
                ''')
                for i in range (len(items)):
                    print (f'{i+1} - {items[i][0]}')
                break
            NotallowedItem = input ("Enter item by number  >  ")
            AllstdInfo = self._get_students_data()
            for p in AllstdInfo:
                if p['id'] == int(stdId):
                    p["Not Allowed Items"].append(items[int(NotallowedItem)])
        # Serializing json 
        json_object = json.dumps(AllstdInfo, indent = 4)
    
        # Writing to sample.json
        with open('Student_info.json', "w") as outfile:
            outfile.write(json_object)

            


    def print_std_info(self,data):
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

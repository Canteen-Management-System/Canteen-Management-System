import json
import pandas as pd
from canteen_project.canteen_pos import CanteenSystem
from canteen_project.Store import Store



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
                self.not_allowed_items()
            elif oper == "B":
                self.buy_daily_meal()
            else:
                continue


        
    def buy_daily_meal(self):
        pass

    def not_allowed_items(self):
        C1 = CanteenSystem()
        print("*  Choose the Not allowed list of Items  *")
        while (True):
            Category = input('Enter category Hot food (H), Snacks (S), Drinks (d), Submit (S)')
            if Category == "S":
                break
            if Category.lower() == 'h':
                table, items = C1.menu('Hot food')
                print(table)
                Category = C1._chosen_item(items)
            if Category.lower() == 's':
                table, items = C1.menu('Snacks')
                print(table)
                Category = C1._chosen_item(items)
            if Category.lower() == 'd':
                table, items = C1.menu('Drinks')
                print(table)

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

import json
import pandas as pd



class Operations:
    def __init__():
        pass

    def recharge():
        pass

    def max_daily_credit(stdid , maxCred):
        P1= ParentPortal()
        AllstdInfo = P1._get_students_data()
        for p in AllstdInfo:
            if p['id'] == int(stdid):
                p["Max Daily Credit"] = float(maxCred)
        # Serializing json 
        json_object = json.dumps(AllstdInfo, indent = 4)
  
        # Writing to sample.json
        with open('/home/student88/CanteenMangmentSystem/Canteen-Management-System/Canteen-project/Student_info.json', "w") as outfile:
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
        self.Balance = 0

    def _get_students_data(self):
        with open('/home/student88/CanteenMangmentSystem/Canteen-Management-System/Canteen-project/Student_info.json', 'r') as f:
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
                Operations.recharge()
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
        pass

    def print_std_info(self,data):
        print(f'''
        Student Info
        _________________
        ID              : {data["id"]}
        Name            : {data["name"]}
        Balance         : {self.Balance} JOD
        Max daily credit: {data["Max Daily Credit"]} JOD
        ''')



if __name__ == '__main__':
    parent1 = ParentPortal()
    parent1.canteen_portal()

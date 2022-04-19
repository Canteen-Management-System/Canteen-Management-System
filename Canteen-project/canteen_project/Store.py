class Store():
    def __init__(self):
        self.menu = "menu"
    
    
    @staticmethod
    def get_items():
        menu= """*  Choose your item  *
                *  1- Item: 1, Price: 0.2 JOD  *
                *  2- Item: 2, Price: 0.5 JOD  *
                *  3- Item: 3, Price: 0.1 JOD  *
                *  4- Item: 4, Price: 0.35 JOD * """
        return menu
    
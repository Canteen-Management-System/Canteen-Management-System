menu = {
    "Hot food": [
        # H11
        {
            'meal 1': {
                'desc': 'fresh soups with wholemeal bread rolls on the side',
                'price': 2.0
            }
        },
        {
            'meal 2': {
                'desc': 'pasta or lasagne with fresh tomato, bolognaise or vegetable-based sauce',
                'price': 2.5
            }
        }
    ],
    'Snacks': {

    },
    "Drinks": [
        {
            'drink 1': {
                'desc': 'Apple',
                'price': 0.35
            }
        },
        {
            'drink 2': {
                'desc': 'Orange',
                'price': 0.35
            },
        }
    ]
}

"""
*  Choose your item  *
*  1- meal 1: fresh soups with wholemeal bread rolls on the side, Price: 0.2 JOD  *
*  2- Item: 2, Price: 0.5 JOD  *
*  3- Item: 3, Price: 0.1 JOD  *
*  4- Item: 4, Price: 0.35 JOD *

"""


class CanteenSystem:

    def __init__(self):
        pass

    @staticmethod
    def greeting():
        greet = (
            '''===================================
   Welcome to the Canteen System
===================================   
              ''')
        print(greet)
        return greet

    def menu(self):
        Store.get_items()
        """_summary_
        """
        pass

    def order(self):
        pass

    def recipe(self):
        pass


if __name__ == '__main__':
    from Store import Store
    CanteenSystem.greeting()

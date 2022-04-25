import pandas as pd
import json


class Store():
    def __init__(self):
        self.menu = "menu"

    def _get_menu_data(self):
        with open('menu.json', 'r') as f:
            menu = json.load(f)
        return menu

    def get_items(self, key):
        items = self._get_menu_data()
        indics = [i for i in range(len(items[key]))]
        table = pd.DataFrame(items[key], indics, items['headers'])
        return table, items[key]

    def online_order(self, stdid, meal, date):
        pass

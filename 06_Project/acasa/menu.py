import json

from acasa.databaseManager import DataBaseManager
from acasa.dish import Dish


class Menu:
    
    def __init__(self) -> None:
        self.menu_dict:dict = {}
        self.menu_list:list = []  # List of Dishes
        self.valid_ids = []
        self.db = DataBaseManager()


    def show_menu(self):
        self.read_menu_from_json()
        self.prepare_menu_list()
        self.show_menu_to_terminal()


    def read_menu_from_json(self):
        file_json_path = "./menu.json"
        with open(file_json_path, mode = "r", encoding= "UTF-8") as file:
            self.menu_dict = json.load(file) 

    def read_menu_from_db(self):
        # DEMO
        sql = "SELECT * FROM DEMO"
        menu = self.db.get_records(sql)


    def prepare_menu_list(self):
        for category in self.menu_dict:           
            for dish_dict in self.menu_dict[category]:
                # create an instance of class Dish --> from the single strings and integers from dictionary dish_dict
                dish = Dish(dish_dict["id"] , dish_dict["title"] , dish_dict["price"])
                self.menu_list.append(dish) 

                # Add the Dish id into a list for later user validation
                self.valid_ids.append(dish.dishid)               
   
    def show_menu_to_terminal(self):
        print("Menu")
        print("~" * 10)
        for dish in self.menu_list:
            print(dish)

  

if __name__ == "__main__":
    
    import os
    from pathlib import Path
    os.chdir(Path(__file__).parent)


    file_json_path = "../menu.json"
    with open(file_json_path, mode = "r", encoding= "UTF-8") as file:
        menu = json.load(file)
        
        for category in menu:
            print(category)
            print("~" * 10)
            for dish_dict in menu[category]:
                # create an instance of class Dish --> from the single strings and integers from dictionary dish_dict
                dish = Dish(dish_dict["id"] , dish_dict["title"] , dish_dict["price"])
                print(dish)
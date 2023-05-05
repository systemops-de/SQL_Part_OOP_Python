import os
from pathlib import Path

from acasa.customer import Customer
from acasa.menu import Menu
from acasa.order import Order

os.chdir(Path(__file__).parent)



def greeting():
    
    print("Willkommen bei Acasa")
    print("~" * 20)
 

def main():

    # 1. Greeting
    greeting()

    # 2. Get Gast information
    customer = Customer()
    customer.get_customer_info()
    customer.insert_customer_into_db()

    # 3. Show Menu
    menu = Menu() 
    menu.show_menu()


    # 4. Get User wishes
    order1 = Order(customer, menu)
    order1.get_user_wishes()
    

    # 5. Receipt Phase
    order1.print_save_receipt()
    


if __name__ == "__main__":
    main()










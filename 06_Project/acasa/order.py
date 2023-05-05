from acasa.customer import Customer
from acasa.databaseManager import DataBaseManager


class Order:
    
    def __init__(self, customer, menu) -> None:
        self.db = DataBaseManager()
        self.customer = customer
        self.user_wish_list = [] # List of ids  example [100, 201, 301]
        self.menu = menu  

    def get_user_wishes(self):
        while True:
            user_wish_id = int(input("> "))
            
            # Exit Point
            if user_wish_id == 0:
                break 

            # Check if the user wish id is available
            if user_wish_id not in self.menu.valid_ids:
                print("Wir bieten das leider nicht!")
                continue


            self.user_wish_list.append(user_wish_id)

        self.user_wish_list.sort()


    def print_save_receipt(self, save_file = True):

        #TODO: Externize Receipt generation to a next class called : receipt

        # 1. Generate Text
        receipt_text = self.generate_receipt_text()

        # 2. Print Text
        print(receipt_text)

        # 3. Save text to file
        if save_file:
            self.save_receipt_to_text(receipt_text)


    def generate_receipt_text(self):
        total = 0
        receipt_text = ""

        # Receipt Header
        receipt_text += "\nQuittung\n"
        receipt_text += "~" * 10 + "\n"

        # Receipt Customer       
        
        receipt_text += f"Kunde: {self.customer.first_name} {self.customer.last_name}\n \n"

        # Receipt Body (Orders)
        receipt_text += "Bestellungen\n"
        receipt_text += "~" * 10 + "\n"
        for user_wish_id in self.user_wish_list:
            for dish in self.menu.menu_list:
                if user_wish_id == dish.dishid:
                    receipt_text += str(dish) + "\n"
                    total += dish.price

        # Receipt Footer
        receipt_text += f"\nTotal : {round(total, 2)}€"

        receipt_text += "\nVielen Dank für Ihren Besuch"

        return receipt_text


    def save_receipt_to_text(self, receipt_text):
        file_name = f"receipt_{self.customer.first_name}_{self.customer.last_name}"

        with open(f"./receipts/{file_name}.txt", mode = "w", encoding= "UTF-8") as file:
            file.write(receipt_text)
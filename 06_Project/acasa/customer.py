from acasa.databaseManager import DataBaseManager


class Customer:
    def __init__(self) -> None:

        # Instance based attributes
        self.customer_id = 0
        self.first_name = "" 
        self.last_name = ""
        self.db = DataBaseManager()

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_customer_info(self):
        self.first_name = input("Enter your first name: ").strip().title()
        self.last_name = input("Enter your last name: ").strip().upper()

    def insert_customer_into_db(self):
        sql = "INSERT INTO Customer(FirstName, LastName) VALUES (?,?);"
        
        data = (self.first_name, self.last_name)

        # Insert the Customer into DB and Return the Inserted Primary Key of the customer
        self.customer_id = self.db.insert_record(sql, data)


if __name__ == "__main__":
    cust1 = Customer()
    cust1.get_customer_info()

    print(cust1)
    
import sqlite3


class DataBaseManager:
    
    def __init__(self, db_path = "./acasaDB.db") -> None:
        
        db_path = db_path

        self.conn = sqlite3.connect(db_path) # 1. 
        self.cursor = self.conn.cursor()  # 2.


    def insert_record(self, sql:str, data):     
        
        """
        with self.conn: #  without commit
            self.cursor.execute(sql, data)
        """
        
       

        try:  
            self.cursor.execute(sql, data)             
        except sqlite3.Error as err:
            print(err)
        else:
            self.conn.commit()
        

        return self.cursor.lastrowid # gets the inserted Primary Key



    def get_records(self, sql):
        pass



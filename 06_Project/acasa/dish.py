class Dish:

    def __init__(self, dish_id, title, price) -> None:
        self.dishid = dish_id 
        self.title = title
        self.price = price
     
    def __repr__(self):
        return f"{self.dishid}. {self.title}\t{self.price}€"
   
   


if __name__ == "__main__":
    dish = Dish(100, "Pizza Margeritta", 5)  
    
    print(dish)  

  
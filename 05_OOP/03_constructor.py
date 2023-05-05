""" 
__init__() : 
- should not include return , because python internally returns AN INSTANCE of the required Class
- belongs to the magic methods --> tbc

Uses cases:
- I can FORCE/Garantee Must fields during construction of an instance
- I can define for each instance all required attributes --> example: project_list 

"""

class Mitarbieter:

    
    def __init__(self, first_name, last_name, location = "Berlin"):  # constructor
        self.first_name = first_name
        self.last_name = last_name 
        self.location = location

        # empty place holders -> to make sure that every instance has these attributes
        self.project_list = []
        self.car = ""
      

    def get_information(self):
        print("MA: ", self.first_name, self.last_name)



# Create an Instance
ma_thomas = Mitarbieter("Thomas", "Meier")  # MUSS Felder  --> constructor __init__() custom constructor
ma_sara = Mitarbieter("Sara", "Meier") 
ma_matthias = Mitarbieter("Matthias", "Meier", "Aachen")


ma_thomas.get_information()
ma_sara.get_information()


ma_thomas.project_list = ["Project 1", "Project 2", "Project 3"]
ma_sara.project_list = ["Project 2"]

ma_list = [ma_thomas, ma_sara, ma_matthias]


# Mitarbeiter karte
for mitarbeiter in ma_list:
    # basic Information
    print(mitarbeiter.first_name, mitarbeiter.last_name, mitarbeiter.location)
    print("~" * 10)

    # Project List

    for project in mitarbeiter.project_list:
        print(project)





 
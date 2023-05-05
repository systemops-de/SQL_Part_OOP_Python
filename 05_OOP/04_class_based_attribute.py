class Mitarbeiter:

    bonus = 500 # class based/shared attribute

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name 
        


    def greeting(self):
        print("Hallo", self.first_name, self.last_name)
        
    
    
    def get_information(self):
        print("MA: ", self.first_name, self.last_name)

    
# Create Instance

ma_thomas = Mitarbeiter("Thomas", "Meier")
ma_sara = Mitarbeiter("Sara", "Meier")
ma_ingo = Mitarbeiter("Ingo", "Meier")

#__dict__ : shows which attributes in there
print(ma_thomas.__dict__)
print(ma_sara.__dict__)
print(ma_ingo.__dict__)

# Read Only for the class based attributes
print(ma_thomas.first_name, ma_thomas.bonus) 
print(ma_sara.first_name, ma_sara.bonus)
print(ma_ingo.first_name, ma_ingo.bonus)

print()

###############################################
# Change the class based attribute via the CLASS itself (not via the instance)
# Increase the value for all Employees
Mitarbeiter.bonus = 700 

print(ma_thomas.__dict__)
print(ma_sara.__dict__)
print(ma_ingo.__dict__)

print(ma_thomas.first_name, ma_thomas.bonus) # 700
print(ma_sara.first_name, ma_sara.bonus) # 700
print(ma_ingo.first_name, ma_ingo.bonus) # 700

print()

###############################################
# Change the class based attribute value via the instance --> it will create a LOCAL instance based attribute with the new value
# Increase the value for specific Employee (Instance)

ma_thomas.bonus = 900 # will be added to the instance profile/attributes to Thomas


print(ma_thomas.__dict__)
print(ma_sara.__dict__)
print(ma_ingo.__dict__)



print(ma_thomas.first_name, ma_thomas.bonus) # 900 # {'first_name': 'Thomas', 'last_name': 'Meier', 'bonus': 900}
print(ma_sara.first_name, ma_sara.bonus) # 700 {'first_name': 'Sara', 'last_name': 'Meier'}
print(ma_ingo.first_name, ma_ingo.bonus) # 700 {'first_name': 'Ingo', 'last_name': 'Meier'}

print()
####################################################
# Change the Class based attribute --> will affect only the instances which does not have the same attribute name
# Change for all instances the value
Mitarbeiter.bonus = 1500 



print(ma_thomas.__dict__)
print(ma_sara.__dict__)
print(ma_ingo.__dict__)

print(ma_thomas.first_name, ma_thomas.bonus) # 900
print(ma_sara.first_name, ma_sara.bonus) # 1500
print(ma_ingo.first_name, ma_ingo.bonus) # 1500



""" 
Instance based Attribute (Instance Shared Attribute)
~~~~~~~~~~~~~~~~~~~~~
self.attribute:
1. Instance based attribute: every instance will get its own(self) value
2. THe instance based attributes are like PUBLIC variables within the class --> other instance based methods can access self.attributes
3. Shared between all methods

Instance based methods
~~~~~~~~~~~~~~~~~~~~
1. the first paramenter should be 'self'
2. this gives the method access to all self.attributes (instance based attributes)
"""

class Car:
    
    def set_information(self, kz, color):
        self.mykz = kz 
        self.mycolor = color

    def get_information(self):        
        print("Car: " ,self.mykz, self.mycolor)



# Create Instances
car1 = Car()   ###-> AA12345
car2 = Car()   ###-> BB12345
car3 = Car()   ###-> CC12345


car1.set_information("AA1234", "Red")
car2.set_information("BB2345", "Black")
car3.set_information("CC2345", "Blue")



car1.get_information()
car2.get_information()
car3.get_information()




 


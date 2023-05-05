class Car:
    pass 

 

# Create Instances
vw1 = Car()
vw2 = Car()
vw3 = Car()

 
 
# Add manual attributes

vw1.kz = "AA12345"
vw1.color = "Red"

vw2.kz = "BB12345"
vw2.color = "Black"

vw3.kz = "CC12345"
vw3.color = "Orange"


# Create a Python List -> of Car instances
car_list = [vw1, vw2, vw3]

# Loop over cars in the car list 
for car in car_list:
    print(car.kz, car.color)

print()
########################################
# Very Bad :



# Create Instances
vw1 = Car()
vw2 = Car()
vw3 = Car()

# Add manual attributes
vw1.kz = "AA12345"
vw1.color = "Red"
vw1.bj = 2020

vw2.kz = "BB12345"
vw2.color = "Black"
vw2.bj = 2021

vw3.kz = "CC12345"
vw3.color = "Orange"
# bj is not there for vw3

# Create a Python List -> of Car instances
car_list = [vw1, vw2, vw3]

# Loop over cars in the car list 
for car in car_list:
    print(car.kz, car.color, car.bj) # ERROR : because vw3 does not have attribute bj

 
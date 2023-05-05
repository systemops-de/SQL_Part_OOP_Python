class Mitarbeiter:

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name 

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def create_emp_via_white_space(cls, emp_string):
        first_name, last_name = emp_string.split()   
        return cls(first_name, last_name)     ###-> go to __init__
   
    @classmethod
    def create_emp_via_underscore(cls, emp_string):
        first_name, last_name = emp_string.split("-") 
        return cls(first_name, last_name)     ###-> go to __init__



# Consumer
ma_thomas = Mitarbeiter("Thomas", "Meier")
ma_thomas = Mitarbeiter.create_emp_via_white_space("Thomas Meier")
ma_thomas = Mitarbeiter.create_emp_via_underscore("Thomas-Meier")


print(ma_thomas)


################################
import pandas as pd

dataframe = pd.DataFrame()  # __init__
dataframe = pd.read_csv()
dataframe = pd.read_excel()
dataframe = pd.read_json()
from pydantic import validate_arguments
from typing import Union

@validate_arguments
def soma(x:int, y:int):
    return  x + y

# soma(1+2)


# dictionary
d = {'a':1,'b':2}
print(d['a'])

# Python code to demonstrate namedtuple()

from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
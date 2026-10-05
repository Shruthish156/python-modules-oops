#MOdules
#modlues means it is a simple .py
#it contain variables,functions,loop

#difference of modules and packages
#1.modules: it is asimple .py  and exaple : name.py
#packages : it is a collection of modules(it contain lot of .py files/folders) and exaple : module(folder) / name.py files

#IMPORT MATH
#it mainly use for import entire maths
import math
print(math.sqrt(16))              #square root
print(math.pow(2,3))              #2 to the power of three
print(math.factorial(85))
print(math.pi)

#FROM MATH IMPORT
#it is mainly use for import the which one needed and necessary 
from math import sqrt,pow,pi,factorial
print(sqrt(81))
print(pow(2,6))
print(pi)
print(factorial(3))

#utils.py
#the main purpose is if we use same function code in different files we can easy to import/access use utils
#from utils import <function name>
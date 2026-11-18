#DECORATOR : 
# it is a function that add or modify the another function without change the originnal code or features
def my_decorator(func):             #decorator function
    def wrapper_name():                  #add extra functionality
        if_checked_login=True
        if if_checked_login:
            print("Login successfull")
            func()
        else:
            print("login again with valid data")
    return wrapper_name                 #it will return wrapper to outer function 
def dash_board():                   #origin function
    print("Welcome to the login page dash_board")
dash_board=my_decorator(dash_board)
dash_board()

print()

#In decorator extra functionality add in inside wrapper function

#functools.wrap : it is use to preserve or save the original functon name and documntation()
#if we not use functools.wrap.Forcebly access the function name it give wrapper function name
from functools import wraps
def my_decorator(func):                  #decorator function
    @wraps(func)                         #it save the origin function information 
    def wrapper_name():                  #add extra functionality
        if_checked_login=True
        if if_checked_login:
            print("Login successfully")
            func()
        else:
            print("login again with valid data")
    return wrapper_name                 #it will return wrapper to outer function 
def dash_board():                        #origin function
    "Hi welcome to lofin dash board features"                 
    print("Welcome to the login page dash_board")
dash_board=my_decorator(dash_board)
dash_board()
print(dash_board.__name__)  #it give wrapper name bcz not use functools.wrap
print(dash_board.__doc__)
#thankyou
        

        
                                 

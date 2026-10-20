#ERROR HANDLING
#define : it is a process of detecting and managing the errors in a program

#VALUE ERRROR : wrong value on the type
try:
    num=int(input("enter a number: "))
    number=10/num
    add="6"+number
    list=[1,2,5,8]
    print(list[4])
    student_marks={"ramu":89,"summu":89,"shruthisha":99}
    print(student_marks["shruthishaaieng"])

except ValueError:                                    #value error
    print("The entering number is invalid!!")

except ZeroDivisionError:                            #zero division error
    print("The number is not divide by zero")

except TypeError:                                    #type error
    print("Can't we add int and string")

except IndexError:                                   #index error
    print("The entering number index is out of range")

except KeyError:                                     #key error
    print("The entering key name is not found")

except AttributeError:                               #attribute error
    print("The method is not found")

finally:                                             #it always be printed even error occur or not
    print("Completed all error handling")


#raise
try:
    age=18
    if age>=18:
        raise TypeError("you are eligeble for election")

    else:
        raise TypeError("not able to add election part")

except TypeError as e:
    print("your age is valid : ",e)

finally:
    print("thankyou for election age enquiring85")

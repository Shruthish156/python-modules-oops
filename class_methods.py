#methods
#means we write function  in inside class
#CLASS METHOD

class Student:
    clg="Sir Mvit"                  #class data
    @classmethod             
    def show_clg(name):             #class method
        return name.clg
college_name=Student.show_clg()     #function calling
print(college_name)

print()

#INSTANCE Method
#it is works with object data  and use self:
class Student_name:
    def __init__(self,name):          #instance data
        self.name=name
    def show_student_name(self):      #instance method
        return self.name
s1=Student_name("AIENGSHRUTHISHA")
show_name=s1.show_student_name()      #function calling
print(show_name)
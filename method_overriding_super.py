#overridings
#define : when child class define methods with same name as its parent class
class student_system:
    def college_topper(self):
        print("he is topper")

class student_management(student_system):
    def college_topper(self):
        super().college_topper()          #it will use to access the both class methods when they have same
        print("he is average topper")

s1=student_management()
s1.college_topper()     
#before using super() it print only he is average topper because method overriding use same methods for both classes

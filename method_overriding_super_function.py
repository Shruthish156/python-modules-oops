#overriding
#define : we use same methods for different classes and try to access it that timings happen overriding
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
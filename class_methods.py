#methods
#means we write function  in inside class
#CLASS METHOD

class Student:
    clg="Sir Mvit"
    @classmethod
    def show_clg(name):
        return name.clg
college_name=Student.show_clg()
print(college_name)
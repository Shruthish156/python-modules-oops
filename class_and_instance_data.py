#CLASS DATA
#define: class data means variable that belongs to all objects in class or shared by all objects in class
class student:
    college="sir MVIT"           #class data -use variable college
s1=student()
s2=student()
print(s1.college)
print(s2.college)
'''
we access the object withput use self that is class data 
both sl and s2 are object they have shared with same variable like "college" that is class data
'''
print()
#INSTANCE DATA
#define: variable that belongs to individual object in class 
class student:
    def __init__(self,name,roll_no):    #instance data
        self.name=name
        self.roll_no=roll_no
s1=student("shruthisha",43)
s2=student("summu",12)
print(s1.name)
print(s1.roll_no)
print(s2.name)
print(s2.roll_no)
'''
we  access the object use self
'''

#REAL case exaple
'''
IN  college students are belongs to different names but college is only one name 
college is class data but students are instance data
'''
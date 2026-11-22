#Type Hints :
"""
type hints means it is annotation that specify the expected types of variable ,funtion parametrs,return values in python

"""
def add_number(a:int,b:int) ->int:   #a and b is specify the values in int type and resturn values should be in int 
    return a+b
result=add_number(10,12)
print(result)

#different types 
#list[int] :[1,2,5,5]
#tuple[int] :(1,4,5)
#set[str]  : {"ramu","raju"}
#dict[str,int] :{"ramu":20,"raju":50} #key is string and values in list

#None Type Hints
#it use when there is no return the any values/names
def animal_name(animal:str) ->None:
    print(f"the king of the forest is {animal}")
animal_name("LION")

def with_draw(amounts :list[int]) ->None:
    for amount in amounts:
        if amount>=0:
            if amount:
                amount -=100
                print(f"the total remaining amount is: {amount}")
            else:
                print("thank you for bank users")

        else:
            print("the amount is not sufficient plase add amount to your bank acc")
with_draw([200,500,-100,12])

#str | none type hints 
#it five either str or none based on condition
subject_marks: dict[str,int] ={
    "kannada":98,
    "english":99,
    "hindi":88,
    "python":100
}
for mark in subject_marks.values():
    if mark>95:

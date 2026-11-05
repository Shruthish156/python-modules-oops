#ITERATOR : it means it is an object return the elements/values at time using next()
#iterable : it means it is an object it allow access the values/elements one by one 
list=[1,8,6,8,7]     #list is  itrerable 
result=iter(list)    #result is iterator . convert list as iterator use iter(built in function)

print(next(result))  #next  decide the stop & print the next values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
# print(next(result)) if use it it give StopIteration bcz only five elemets are present in list

print()
#crete our custom iterator it contain two parts __iter__() ,and __next__()
list1=[1,2,5,6,8]
iterator=iter(list1)
while True:
    try:
        value=next(iterator)
        if value>=5:
            print(value)

    except StopIteration:
        break

print()       
#generator : it is a type of iterator it generate the values at a time use yield
def number():
    yield 20          
    yield 25
    yield 30
for value in number():
    print(value)

'''
"yield" is print the all the values and it do resume the iteratin from where it is stopped but "return" is terminate and stop
'''
#generator comphrension
generator_comphrension=(x**2 for x in range(1,20) if x%2==0)
for values in generator_comphrension:
    print(values,end=" ")
 
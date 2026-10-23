#FILE HANDLING : 
"""
it is a process of reading,writing,creating the files and adding the data in existing files using programing language

"""

#1.writing "w" : it is create the files if not exist,if exist it remove the data add current data and save it
with open ("aishruthisha.py","w") as file:
    file.write("welcome to the ai engineering\n")
#2.append add the data "a"
with open("aishruthisha.py","a") as file:
    file.write("good boy")
#3 read the data "r"
with open("aishruthisha.py","r") as file:
    print(file.read())
#4 creating the file "x"
with open("shru01.py","w") as file:
    file.write("shruthisha")

try:
    with open("encapsulation.py","x") as file:
        print("hello")

except FileNotFoundError as e:
    print(f"file is nor exist crete file {e}")

except FileExistsError as e:
    print(f"file is exist {e}")

finally:
    print("completed")
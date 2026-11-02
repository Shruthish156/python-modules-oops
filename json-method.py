#JSON :javascript object notation
#it is use to store and transfer the data froom one applicaion to another application
#4 mthods(types)
"""
1.json.dumps : dictionary to string (data,indent)
2.json.dump: dictionary to file (dat,file,indent)
3.json loads: string to dictionary
4.json.load:file to dictionary
"""
#1. dumps : dictionary to string
import json
payment_methods={
    "upi":5000,
    "net_bank":5500,
    "phone_pe":6000,
    "credit_card":50000
    }
result=json.dumps(payment_methods,indent=4)
print(result)
print(type(result))

#2.dump :dictionary to file
import json 
payment_methods={
    "upi":5000,
    "net_bank":5500,
    "phone_pe":6000,
    "credit_card":50000
    }
with open("python.json1","w",encoding="utf-8") as file:
    json.dump(payment_methods,file,indent=4)

#3 loads : string to dictionary
import json
student_marks='{"ramu":85,"raju":80,"summu":85,"ramu":85,"shruthisha":95}'
result=json.loads(student_marks)
print(result)

#4 load : file to dictionary
import json
with open("python.json1","r",encoding="utf-8") as file:
    data=json.load(file)
    print(data)
    print(data["upi"])
    print(type(data))





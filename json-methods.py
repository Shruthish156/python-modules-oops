#FILE CREATION
import json 
payment_methods={
    "upi":5000,
    "net_bank":5500,
    "phone_pe":6000,
    "credit_card":50000
    }
with open("python.json1","w",encoding="utf-8") as file:
    json.dump(payment_methods,file,indent=4)


#ADD NEW DATA
#read the data
with open("python.json1","r",encoding="utf-8") as file:
    payment=json.load(file)

#add new data
payment["net_banking"]=100000
#payment.update(payment)
#or we can use payment

#write the data
with open("python.json1","w",encoding="utf-8") as file:
    json.dump(payment,file,indent=4)
print(payment)

#UPDATE/CHANGES
import json
with open("python.json1","r",encoding="utf-8") as file:
    payments=json.load(file)

#update/changes
if payments["phone_pe"]==6000:
    payments["phone_pe"]=36000
    
#write the data
with open("python.json1","w",encoding="utf-8") as file:
    json.dump(payments,file,indent=4)

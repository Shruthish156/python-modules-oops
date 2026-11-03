#jsonl 
#it means it store the each object new line by line
#there us no need an array(list)
#usually use .jsonl

#dictionary to strings
import json
data={"name":"shruthisha",
      "age":20,
      "profession":"aiengineering"}
result=json.dumps(data)
print(result)
print()
#string to dictionary
data='''{"name":"shruthisha",
      "age":20,
      "profession":"aiengineering"}'''
results=json.loads(data)
print(results)

#dictionary to file
data1={"name":"shruthisha","age":20,"profession":"aiengineering"}
data2={"name":"shruthisha","age":20,"profession":"aiengineering"}
with open("files.jsonl","w",encoding="utf-8") as file:
    for data in [data1,data2]:
        json.dump(data,file)
        file.write("\n")
print()
#file to dictionary
with open("files.jsonl","r",encoding="utf-8") as file:
    for line in file:
        result=json.loads(line)
        print(result)

#add data in existing file
data1={"company":"google"}
data2={"company_role":"AI_ENG_software"}

data=[data1,data2]

#append the data
with open("files.jsonl","a",encoding="utf-8") as file:
    for datas in data:
        json.dump(datas,file)
        file.write("\n")
        print(datas)

#change the data or update the data
#read existing file
data=[]
with open("files.jsonl","r",encoding="utf-8") as file:
    for line in file:
        data.append(json.loads(line))  #add data to existing file

#changes
data[3]["company_role"]="GENAI_ENG"

#write the data
with open("files.jsonl","w",encoding="utf-8") as file:
    for datas in data:
        json.dump(datas,file)
        file.write("\n")
        print(datas)
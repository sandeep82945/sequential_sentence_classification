import json 

filename="/content/sequential_sentence_classification/data/CSAbstruct/test.jsonl"
num = sum(1 for line in open(filename))
import math          
num  = math.ceil(num/4) 

f = open ('/content/sequential_sentence_classification/actual.json', "r") 
# Reading from file 
data = json.loads(f.read()) 
filtered_actual = data[-num:]
f.close()

f2= open ('/content/sequential_sentence_classification/predicted.json', "r") 
data = json.loads(f2.read()) 
filtered_predicted = data[-num:]
# returns JSON object as  
# a dictionary 
print(filtered_actual)
print(filtered_predicted)
print("************************")
# for item in zip(filtered_actual,filtered_predicted):
#     print(item)
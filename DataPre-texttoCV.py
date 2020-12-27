import numpy 
import pandas as pd

mcqs=[]
str=""
with open('CS_DS-AI.txt','r') as file:
    str=file.read()
temp=""
for i in range(0,len(str)-1):
    if str[i]=='\n' and str[i+1]=='\n':
        mcqs.append(temp)
        temp=""
    else:
        temp+=str[i]+'\n'
with open('file.txt','w') as file:
    file.write(temp)
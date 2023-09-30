from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


for i in contacts_list:
    pattern = r"([+]?[78])\s*[(]?(\d{3})[)]?\s*[-]?(\d{3})[-]?(\d{2})[-]?(\d{2})[\s(]*([доб.]*)\s*([\d]*)[)]?"
    repl = r"\1(\2)\3-\4-\5 \6\7"
    result = re.sub(pattern,repl,i[5])
    i[5]=result.strip()
for j in contacts_list:
    s = " ".join([j[0],j[1],j[2]])
    result = s.split()
    for count,k in enumerate(result):
       j[count] = result[count]       
contacts_list2 = []
d = []
for k in contacts_list:       
  d += k
s = " ".join(d)           
pattern2 = r"(\b[а-яёА-Я]+)\s([а-яёА-Я]+)\s([\w]*)\s(\w*\s+\S+\s+[доб.]*\d*)([\s\S]*)\1\s\2\s\3?\s\w*"     
repl2 =  r"\1 \2 \3 \4"
result2 = re.sub(pattern2,repl2,s)
pattern3 = r"([luй])\s+([УЬМЛП])"     
repl3 =  r"\1   \2"
result3 = re.sub(pattern3,repl3,result2).split("  ")
a = result3[0].split()
b = result3[1].split(maxsplit=4)
b1 = b[4].split("+")
b.pop()
b.append(b1[0])
b2 = b1[1].split()
b.append("+"+b2[0])
b.append(b2[1])

c = result3[2].split()
c.append(result3[3])
c.append(result3[4])
f = result3[5].split()
f1 = result3[6].split()
f.append(f1[0]+f1[1])
f.append(f1[2])
g = result3[7].split()
g1 = result3[8].split()
g.append(g1[0])
g.append(g1[1])
e = result3[9].split()
e.append(result3[10])
e.append(result3[11])   

contacts_list2.append(a)
contacts_list2.append(b)
contacts_list2.append(c)
contacts_list2.append(f)
contacts_list2.append(g)
contacts_list2.append(e) 
  

with open("phonebook.csv", "w",encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  

  datawriter.writerows(contacts_list2)

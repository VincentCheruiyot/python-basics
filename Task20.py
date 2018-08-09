file = open("pythondata2.csv","r")
from  Task17 import Person
persons=[]
lines= file.readlines()
for line in lines:
    values = line.split(',')
    # print(values[0], values[2])
    x= Person(values[0], values[2])
    persons.append(x)

file.close()

for person in persons:
    person.sayHi()
    person.printDetails()
#split







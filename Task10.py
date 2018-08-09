#around and around as per video no. 19
#for loop let's do an action a certain number of times
#while loop runs unknown number of times until the condition becomes faulty

my_list=['hello','how','are','you']
for word in my_list:
    print(word)

for letter in 'abcdefghijklmnopqrstuvwxyz':
    print(letter)

start=10
while start:
    print(start)
    start-=1

names=['Vincent','Cheruiyot','Koech','Mise']
for name in names:
    if name=='Mise':
        break
    print(name)

for name in names:
    if name == 'Mise':
        continue
    print(name)

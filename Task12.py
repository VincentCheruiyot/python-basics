#fully functional program as per video no. 21

def hows_the_puppy():
    print("He's pining for the fjords!")


hows_the_puppy()

def lumberjack(name):
    if name.lower()=='vin':
        print("Vin's a lumberjack and he's OK!")
    else:
        print("{} sleeps all night and {} works all day!".format(name, name))

lumberjack("Maureen")

def lumberjack(name, pronoun):
    print("{}'s a lumberjack and {} OK!".format(name, pronoun))

    print(lumberjack())

def average(num1,num2):
    return (num1+num2)/2

avg=average(2,8)
print(avg)



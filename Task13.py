#exception rule as per video no. 22
#exception halts the entire program

#users' input brings more problem cos they are quite unpredicatble

try:
    count=int(input("Give me a number: "))
except ValueError:
    print("That's not a number!")
else:
    print("Hi "*count)

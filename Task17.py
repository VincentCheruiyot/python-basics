class Person:
    def __init__(self, names, age):
        self.names=names
        self.age=age

    def printDetails(self):
        print(self.names,self.age)

    def sayHi(self):
        print("Hi", self.names)



# p1= Person("John",12) #constructor
# p2= Person("Mary",19)
#
# p1.printDetails()
# p2.sayHi()
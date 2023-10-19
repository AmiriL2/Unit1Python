"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
# create a class called person
class Person:
    #give it an attribute
    species = 'Homosapien'
    #define 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
#give a value to the variable "Amiri"
Amiri = Person("Amiri Layne", 17)

#print out the end result
print("Hi my name is", Amiri.name, "and I am", Amiri.age, "years old")
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
#create animal class for all animals
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass
    
#subclass under animal
class Dog(Animal):
    #define the method as speak
    def speak(self): 
        #put what the method should print 
        print("The dog barks")
    
#subclass under animal
class Cat(Animal):
    #define the method as speak
    def speak (self):
        #put what the method should print
        print("The cat meows")

#give the cat and dog a value
CatObject = Cat("Bailey")
DogObject = Dog("Barry")

#call on the method to make it print what you want them to print
CatObject.speak()
DogObject.speak()


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
# create a class called BankAccount
class BankAccount: 

   # give it attributes like "Name" and "Balance"
    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner

    #define the balance of the bank account
    def balances(self): 
        #print out what your current balance is
        print("Your current balace is: ", self.balance)
    
    #give value to the deposite option
    def deposit(self, depo):

        #deposit = add in so subtract from balance
        self.balance = self.balance + depo
    #give value to withdraw option
    def withdraw(self, withdraw):
        #withdraw = take out so subtract from balance
        self.balance = self.balance - withdraw
         #print out what your current balance is
        print("Your new balance is: ", self.balance)

#give value to the bank account (Name and Balance)
AmiriBank = BankAccount("Amiri", 13204.23)

AmiriBank.balances()
AmiriBank.deposit(234)
AmiriBank.withdraw(50)
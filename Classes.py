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
        
Amiri = Person("Amiri Layne", 17)

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
class BankAccount: 
    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner
    def balances(self): 
        print("Your current balace is: ", self.balance)
    def deposit(self, depo):

        self.balance = self.balance + depo
    def withdraw(self, withdraw):
        self.balance = self.balance - withdraw
        print("Your new balance is: ", self.balance)

AmiriBank = BankAccount("Amiri", 13204.23)

AmiriBank.balances()
AmiriBank.deposit(234)
AmiriBank.withdraw(50)
ToDo = ["get cash, spend cash, cry"]

# allow the user to add whatever they want to the list
while True:
    todoinput = input("Would you like to add or remove a todo?")
    if todoinput == ("add"):
        #if user types add, ask what is new todo
        ADD = input("what is your new todo? ")
    #append to add new todo
        ToDo.append(ADD)
    #if user types remove, ask what they would like to remove
    elif todoinput == ("remove"):
        #if user types add, ask would you like to remove
        REMOVE = input("what would you like to remove? ")
    #remove from todo list
        ToDo.remove(REMOVE)
    

    else: 
        print("Incorrect Input")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("your current todos are: " 
          
    + str(ToDo)) 






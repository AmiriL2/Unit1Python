ToDo = [""]

#condition has to be true to reprint when done
while True:

    # allow the user to add whatever they want to the list
    print("")
    todoinput = input("Would you like to add or remove a todo?")
    print("")
    if todoinput == ("add"):

        #if user types add, ask what is new todo
        ADD = input("what is your new todo? ")

        #append to add new todo
        ToDo.append(ADD)

    #if user types remove, ask what they would like to remove
    elif todoinput == ("remove"):

        #if user types add, ask would you like to remove
        REMOVE = input("what would you like to remove? ")
        print("")
        #put if statement so that if the input is in the list, it becomes removed
        if REMOVE in ToDo:
        
            #remove from todo list 
            ToDo.remove(REMOVE)
        
        #if neither of the conditions are true then print the error
        else:
            print("Error: This is not in the list")
            print("")

    #if none of these conditions are true then you print that the input is incorrect
    else: 
        print("Incorrect Input")
        print("")
        print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")

    #print what the current todos are after something was added or removed
    print("Your current todos are: " )
    X = 1 

    #this allows it to count the number of items in the list 
    for T in ToDo:

        #X is converted to a string so that it is able to be printed out
        #T is printed so that it prints whatever is in the list 
        print(str(X) + ") " + T)

        #add one every time a new item is added to the list
        X +=1






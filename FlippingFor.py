"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
#creation of string with random item
name = 'Amiri'

#for loop in t as the characters in the list
for t in name:

    #prints the total
    print(t)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
#this is the list that will be calculated together
list = [10,2,32,44]

#this is so that the original suk is set to zero
sum = 0

#for all the items in numbered list this runs
for d in list:

    #add all the items in the list
    sum += d

    #prints the total
print(sum)


"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
#sentence that will be counted out
sentence = "This is a sentence"

#split would make all the sentence into just words
words = sentence.split()

#for loop to make it print out the word length
for h in words:
    print("Word Length: ", len(h))

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result
"""
#dictionary with keys and values
classmates = {
        'Amiri': 1, 
        'Mekhi': 2, 
        'Shawn': 3, 
        'Khalil': 4} 

# for loop to allow it to print out whatever is in the dictionary
for mates in classmates:

    #print the dictionary
    print(mates)

"""
In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
#This is what i expected because I wanted it to 
#print just the names in the list and thats what it did
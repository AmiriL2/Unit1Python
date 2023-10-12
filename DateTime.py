import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
#print out the date & time now 
print("Today's date is: ", datetime.datetime.now())

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
#set a variable for the time
now = datetime.datetime.now()

#print out the time in a certain format (MM/DD/YYYY)
print("The Current Time is: ", now.strftime("%m/%d/%y %H:%M:%S"))
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
#converts string to datetime
def convert(DateTime):

    #format of date
    format= "%b %d %Y %I:%M%p" 

    #strftime sets the format
    datetimeStr = datetime.datetime.strptime(DateTime, format)

    #this returns the datetimeStr
    return datetimeStr

#variable for first date
dateTime1 = 'Mar 3 2005 8:04AM'

#variable for second date
dateTime2 = "May 31 2006 5:34AM"

#convert function to convert variable
x = convert(dateTime1)
y = convert(dateTime2)

#subtracts one date from another to find difference in date
print(y - x)
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
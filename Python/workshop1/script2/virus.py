import datetime
#imports the datetime module
Current_Date = datetime.datetime.today()
#gets the current date
print ('Current Date: ' + str(Current_Date))
#converts the current date into a string

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
#gets the previous date by subtracting 1 day
print ('Previous Date: ' + str(Previous_Date))
#converts the previous date into a string

NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
#gets the next date by adding 1 day
print ('Next Date: ' + str(NextDay_Date))
#converts the next date into a string
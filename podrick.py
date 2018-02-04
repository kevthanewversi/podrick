#!/usr/bin/env python
#import emoji
import subprocess
import random
import datetime
from dateutil import parser
from dateutil.parser import parse

#pre-requisites sendmail & imported libs
#remember to test for run times in the code of say having the dates data come from a file or from a dict
#game of thrones quote

#check if sendmail/postfix is installed
#should be run once a month and store all the birthdays for that month



birthday_dates = {"apples": "Jan 17 2018", "oranges": "July 10"}
messages = ["Test","Test","Test","Test"]

#use cases to chcek for certain months and check for certain days that match with guys' birthdays
now = datetime.datetime.now()

#consumes csv file and saves it data to a dict
def process_csv(csv_file):
    fieldnames = ['name', 'date']
    data = csv.DictReader(csv_file,fieldnames = fieldnames,dialect='excel')
    for row in data:
        birthday_dates.append(row[name])
        birthday_dates.append(row[date])
    validate_birthday_dates(birthday_dates)
    return True

#store values in dict infinitely
# csv encoding -----check this <<<<<<<<<<

'''
Method that checks if the names and birthdays in the csv file
are strings and aren't empty values 
'''
def validate_birthday_dates(birthday_dates):
    #for key,value in birthday_dates.items():
    count = 0
    for row in birthday_dates.items():
        #code to check if today's date is someones' bday
    #reg expression to check if date is in required format
    #ValueError: time data '' does not match format '%b %d %Y'
    #remove this if data is coming from a CSV
        if type(row[date])!= str | if type (row[name]) != str:
             print(row[name]+"'s birthday isn't a valid date")
        if not row[name] | not row ['data']:
             print("Row %s has an empty/empty values. Enter a name 
                     & birthday date or delete the row before export
                     your excel file to csv format", (count))
        count += count     
     #birthdate = datetime.datetime.strptime(value, '%b %d %Y')
     birthdate = parse(value)
     month = birthdate.month
     day = birthdate.day
     if (month == now.month):
         print(key,value)
     print("It's your birthday month")
     if day == now.day:
         random = random.choice(messages)
         sendmail()


def sendemail():
    process = subprocess.Popen(("echo",random),stdout=subprocess.PIPE)
   output  = subprocess.check_output(( "mail", "-s", "Birthday wishes", "test@gmail.com"), stdin=process.stdout)
   (out, err) = process.communicate()

if __name__ == "__main__":

    #handle this else
   if os.file.isfile("birthdays.csv"):
       csv_file = open("birthdays.csv","r")
       process_csv(csv_file)
   #else:
   #    if not birthday_dates:
   #        print ("Enter some ")
   #sendemail()

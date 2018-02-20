#!/usr/bin/env python
#import emoji
import subprocess
import os
import random
import datetime
import re
from dateutil import parser
from dateutil.parser import parse
from distutils import spawn

#pre-requisites sendmail & imported libs
#remember to test for run times in the code of say having the dates data come from a file or from a dict
#game of thrones quotes

class Podrick:

    birthday_dates = {"apples": "Jan 17 2018", "oranges": "July 10"}
    messages = ["Test", "Test", "Test", "Test"]
    date_re = re.compile('^(0?[1-9]|[12]\d|3[01])-(0?[1-9]|1[0-2])-([12]\d{3})$')

    #use cases to chcek for certain months and check for certain days that match with guys' birthdays
    now = datetime.datetime.now()
    count = 0
    errors = 0
    birthday_dates = []

    '''
     Method that checks if either sendmail/postfix are installed
    '''
    def email_client_check():
        raven1 = spawn.find_executable("sendmail")
        raven2 = spawn.find_executable("postfix")
        if (raven1 is None) & (raven2 is None):
            print("Podrick can't send ravean without either sendmail or postfix")
        return True
    # should be run once a month and store all the birthdays for that month


    # store values in dict infinitely
    # csv encoding -----check this <<<<<<<<<<
    '''
    Method that checks if the names and birthdays in the csv file
    are strings and aren't empty values
    '''
    def validate_birthday_dates(self,birthday_dates):
        # for key,value in birthday_dates.items():
        for row in birthday_dates.items():
            # code to check if today's date is someones' bday
            # reg expression to check if date is in required format
            # ValueError: time data '' does not match format '%b %d %Y'
            # remove this if data is coming from a CSV
            # birthrday_dates here is a list not a dict  so change my validate method call to use the DictReader object
            if type(row[name]) != str | type(row[date]) != str:
                print(row[name]+"'s birthday isn't a valid date")
                self.errors += self.errors
            if not row[name] | row[date]:
                print("""Row %s has an empty/empty values. Enter a name
                        & birthday date or delete the row before export
                        your excel file to csv format""", (self.count))
                self. errors += self.errors
            if not self.date_re.match(row[date]):
                print("The birthday on row %s does not follow the format DD-MM-YYYY", (self.count))
                self.errors += self. errors
            self.count += self.count
            if self.errors:
                print("Please correct the issues above and re-run Podrick")
                break
            else:
                self.birthday_check(row[name], row[date])
    '''
    Consumes csv file and saves it data to a dict
    '''
    def process_csv(self,csv_file):
        fieldnames = ['name', 'date']
        data = csv.DictReader(csv_file,fieldnames = fieldnames,dialect='excel')
        for row in data:
            self.birthday_dates.append(row[name])
            self.birthday_dates.append(row[date])
        self.validate_birthday_dates(self.birthday_dates)
        return True

    '''
    Method that checks if the date today is someone's b-day and sends a birthday email
    '''
    def birthday_check(self, key, value):
        #birthdate = datetime.datetime.strptime(value, '%b %d %Y')
        birthdate = parse(value)
        month = birthdate.month
        day = birthdate.day
        if (month == self.now.month):
            print(key, value)
        print("It's your birthday month")
        if (day == self.now.day):
            rand = random.choice(self.messages)
            self.sendemail(rand)

    '''
    Method that sends out emails
    '''
    def sendemail(self, rand):
        process = subprocess.Popen(("echo", random), stdout=subprocess.PIPE)
        output  = subprocess.check_output(("mail", "-s", "Birthday wishes", "test@gmail.com"), stdin=process.stdout)
        out, err = process.communicate()


if __name__ == "__main__":
    if Podrick().email_client_check():
        # handle this else
        if os.file.isfile("birthdays.csv"):
            csv_file = open('birthdays.csv', 'r')
            Podrick(). process_csv(csv_file)
   #else:
   #    if not birthday_dates:
   #        print ("Enter some ")
   #sendemail()

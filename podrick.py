#!/usr/bin/env python
#import emoji 
import subprocess
import random
import datetime
from dateutil import parser
from dateutil.parser import parse

#pre-requisites sendmail & imported libs
#remember to test for run times in the code of say having the dates data come from a file or from a dict

#check if sendmail/postfix is installed

mydict = {"apples": "Jan 17 2018", "oranges": "July 10"}
messages = ["On your special day, I wish you good luck. I hope this wonderful day will fill up your heart with joy and blessings. Have a fantastic birthday, celebrate the happiness on every day of your life. Happy Birthday!!","Happy Birth","Love","Mamama"]

#use cases to chcek for certain months and check for certain days that match with guys' birthdays
now = datetime.datetime.now()

for key,value in mydict.items():
  #code to check if today's date is someones' bday
  #reg expression to check if date is in required format
  #ValueError: time data '' does not match format '%b %d %Y'
  #remove this if data is coming from a CSV
   if type(value)!= str:
      print(key+"'s birthday isn't a valid date")
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

sendemail()

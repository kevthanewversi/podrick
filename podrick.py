#!/usr/bin/env python
#import emoji 
import subprocess
import random
import datetime
from dateutil import parser

#pre-requisites sendmail & imported libs
#remember to test for run times in the code of say having the dates data come from a file or from a dict

mydict = {"apples": 42, "oranges": 999}
messages = ["On your special day, I wish you good luck. I hope this wonderful day will fill up your heart with joy and blessings. Have a fantastic birthday, celebrate the happiness on every day of your life. Happy Birthday!!","Happy Birth","Love","Mamama"]

#use cases to chcek for certain months and check for certain days that match with guys' birthdays
now = datetime.datetime.now()

for key,value in mydict.items():
  #code to check if today's date is someones' bday
   month = parser.parser(value).month 
   if (month == now.month): 
     print(key,value)
     print("It's your birthday month")
random = random.choice(messages)

def sendemail():
   process = subprocess.Popen(("echo",random),stdout=subprocess.PIPE) 
   output  = subprocess.check_output(( "mail", "-s", "Birthday wishes", "test@gmail.com"), stdin=process.stdout)
   (out, err) = process.communicate()

sendemail()

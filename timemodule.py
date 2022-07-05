#!/usr/bin/python
import time
import calendar

localtime = time.localtime(time.time())
print("Local current time :", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("Formated Local current time :", localtime)

cal = calendar.month(2022, 6)
print("Here is the calendar:")
print(cal)







#Importing Library for today's date
from datetime import date

#Taking input from user
name = input("Please enter your name : ")
bdate = input("Please enter your Birthdate in [dd/mm/yyyy] format with '/' : ")

#Spliting birthdate by /
bday = int(bdate.split("/")[0])
bmonth = int(bdate.split("/")[1])
byear = int(bdate.split("/")[2])

#Spliting birthdate by -
tdate = str(date.today())
tday = int(tdate.split("-")[2])
tmonth = int(tdate.split("-")[1])
tyear = int(tdate.split("-")[0])

#Finding difference of dates
mday = (tday-bday)
mmonth = (tmonth-bmonth) 
myear = (tyear-byear)

#Calculating months 
totalmonth = (mmonth)+(myear*12)

#Calculating days
totalday = int(tday-bday)

#printing outputs 
print(f"Hii, {name.capitalize()}. As of today, your age is {totalmonth} months and {totalday} days")
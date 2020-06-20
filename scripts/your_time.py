from datetime import datetime
import time


current = datetime.fromtimestamp(time.time()).timestamp()
print("enter your day of birthday")
birthday = input("DD/MM/YY")
startdate = int(datetime.strptime(birthday,"%d/%m/%y").timestamp())
print(int((current-startdate)/604800))
age = int(input("how many years do you plan to live?"))
timestampage = age * 365 * 24 * 60 * 60
dayofdie = startdate + timestampage
forlife = dayofdie - current
forlife_days = int(forlife / 60 / 60 / 24)
forlife_weeks =  int(forlife_days / 7)
print("You have",forlife_days,"days for life","and you have",forlife_weeks,"weeks for life")

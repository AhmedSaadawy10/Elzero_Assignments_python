import datetime
# print(dir(datetime))
# print(datetime.datetime.now().date())
current_date =datetime.datetime.now() 
the_date = datetime.datetime(2021,6,25)
the_days = current_date - the_date

print(f"Days from {current_date} to {the_date} is {the_days.days} ")

#________________________________________________________________
#2
print("-"*30)

print(datetime.datetime.now())
print(current_date.strftime("%Y-%m-%d"))
print(current_date.strftime("%Y/%m/%d"))
print(current_date.strftime("%d-%m-%y"))
print(current_date.strftime("%a-%b-%y"))
print(current_date.strftime("%a,%d-%b-%C"))
print(current_date.strftime("(%a,%d)-(%b,%m)-%Y"))
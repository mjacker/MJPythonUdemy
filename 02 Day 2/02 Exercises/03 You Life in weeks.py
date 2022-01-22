age = input("What is your current age?")

monthLeft = ( 90 - int(age) ) * 12
weeksLeft = ( 90 - int(age) ) * 52
daysLeft = ( 90 - int(age) ) * 365

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthLeft} months left.")
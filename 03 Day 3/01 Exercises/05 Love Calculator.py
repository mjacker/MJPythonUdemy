# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

bothName = name1 + name2

pointL = 0
pointR = 0
points = 0

pointL += bothName.count("t")
pointL += bothName.count("r")
pointL += bothName.count("u")
pointL += bothName.count("e")

pointR += bothName.count("l")
pointR += bothName.count("o")
pointR += bothName.count("v")
pointR += bothName.count("e")

print(f"pointL: {pointL}, pointR: {pointR}")

points = int(str(pointL) + str(pointR))

print("points: ", points)

if points < 10 or points > 90:
    print(f"Your score is {points}, you go together like coke and mentos.")
elif points >= 40 and points <= 50:
    print(f"Your score is {points}, you are alright together.")
else:
    print(f"Your score is {points}.")

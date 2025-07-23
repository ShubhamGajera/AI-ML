print('hello')


#04 Intials 
# Write code below 💖
#My name is shubham gajera
# i like to read managa..
print('SSSSS   GGGGGG')
print('S       G    G')
print('S       G     ')
print('SSSSS   G  GGG')
print('    S   G    G')
print('    S   G    G')
print('SSSSS   GGGGGG')

#05 Snali mail
print('21 July 2025')
print('happy.......')
print('want to become AI/ML Engineering')
print('Stay consistent and stay focuesd')
print('😎')

#06 data types
# 06. Data Types
# # Variables
# In programming, variables are used for storing data values. Each variable has a name and holds a value. 📦



# The variable name can consist of letters, numbers, and the _ underscore.

# These are all valid variable names and values:

# name = 'Erlich Bachman'
# user_id = 16180339887
# progress = 0.75
# xp = 60
# verified = True

# The = equal sign means assignment:

# We're assigning the string value 'Erlich Bachman' to the variable name.
# We're assigning the number value 16180339887 to the variable user_id.
# We're assigning the number value 0.75 to the variable progress.
# We're assigning the number value 60 to the variable xp.
# We're assigning the truth value True to the variable verified.
# We can also change the value of a variable, or print it out:

# xp = 70
# xp = 80

# print(xp)    # Output: 80

# Here, we are assigning the number value 70 to the variable xp. Then, we are reassigning the number value 80 to the same variable. And printing it out.

# # Data Types
# ## Integer
# An integer, or int, is a whole number. It has no decimal point and contains the number 0, positive and negative counting numbers. If we were counting the number of people on the bus or the number of jellybeans in a jar, we would use an integer.

# year = 2023
# age = 32

# ## Float
# A floating-point number, or a float, is a decimal number. It can be used to represent fractions or precise measurements. If you were measuring the length and width of the couch, calculating the test score percentage, or storing a baseball player’s batting average, we would use a float instead of an int.

# pi = 3.14159
# meal_cost = 12.99

# ## String
# A string, or str, is used for storing text. Strings are wrapped in double quotes " " or single quotes ' '.

# message = "good nite"
# username = '@snoopdogg'

# When we did printing in the first chapter, we printed a string data type.

# ## Boolean
# A Boolean data type, or bool, stores a value that can only be either true or false. In Python, it's capitalized True or False. It's named after the British mathematician George Boole (1815-1864).

# late_to_class = False
# cranky = True


#07 Temperature
# https://www.google.com/imgres?q=remainder%20in%20python&imgurl=https%3A%2F%2Fmiro.medium.com%2Fv2%2Fresize%3Afit%3A883%2F1*PCtMZ50XVXk-wCiEssumOw.png&imgrefurl=https%3A%2F%2Fmedium.com%2F%40anay.m.tripathi%2Fthe-curious-case-of-modulo-operator-and-negative-numbers-in-python-57e243691b40&docid=Xu8ijFvy5g_AnM&tbnid=d7fVZAfhzhJqIM&vet=12ahUKEwjMmOnO6dCOAxXzma8BHcOdHWcQM3oECA0QAA..i&w=883&h=534&hcb=2&ved=2ahUKEwjMmOnO6dCOAxXzma8BHcOdHWcQM3oECA0QAA
# https://www.google.com/imgres?q=remainder%20in%20python&imgurl=https%3A%2F%2Fblog.teclado.com%2Fcontent%2Fimages%2F2019%2F03%2F10div3-names.png&imgrefurl=https%3A%2F%2Fblog.teclado.com%2Fpythons-modulo-operator-and-floor-division%2F&docid=mKOx7Qx9WC18HM&tbnid=tNDuKHck5_LLLM&vet=12ahUKEwjMmOnO6dCOAxXzma8BHcOdHWcQM3oECBMQAA..i&w=566&h=292&hcb=2&ved=2ahUKEwjMmOnO6dCOAxXzma8BHcOdHWcQM3oECBMQAA
# a=15
# b=7
# print(a%b)
# c=10
# d=20
# print(d/c)

f= 25
Celsius = (f-32) / 1.8
print(Celsius)

#08 Exponents
# Write code below 💖

# a=2**2
# print(a)

m=70
h=1.73
# h2=1.73**2
bmi = m / (h**2)
# bmi2 = m / h2
print(bmi)
# print(bmi2)


# 09 User Input

# Write code below 💖
# name=input('Your name : ')
# print(name)
# age=int(input('enter your age  : '))
# print(age)

# a=int(input('Value of a :'))
# b=int(input('Value of b :'))
# c=(a**2 + b**2) ** 0.5
# print(c)


# Quadratic Formula
a = int(input('Value of a :'))
b = int(input('Value of b :'))
c = int(input('Value of c :'))
root1 = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)  #can use b*b
root2 = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)  # can use b*b
print(root1)
print(root2)

#10 Currency
# Woohoo! You learned variables in Python! 🙌

# Here's a recap of everything we learned in this chapter:

# Data types: int, float, str, bool.
# Arithmetic operators: +, -, *, /.
# The % modulo finds the remainder.
# The ** exponentiation finds the exponent.
# The input() function is used to get user input.
# The int() function converts a value into an integer number.
# Let's put it all together now!

# Write code below 💖

a=int(input("What do you have left in pesos?"))
b=int(input("What do you have left in soles?"))
c=int(input("What do you have left in reais?"))

d=(a/4072.87)+(b/3.55)+(c/5.58)

print(d)

# from github of codedex

# pesos = int(input('What do you have left in pesos? '))
# soles = int(input('What do you have left in soles? '))
# reais = int(input('What do you have left in reais? '))

# total = pesos * 0.00025 + soles * 0.28 + reais * 0.21

# print(total)

#11 Coin flip

# Write code below 💖

import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')

  a = 17

# if (a%2==1):
#       print('odd')
# else:
#     print('even')

# 12 Grades

# Write code below 💖

grade=int(input("Tell Your Grade : "))

if(grade >= 55):
  print("You Passed✌️")
else:
  print("You failed")
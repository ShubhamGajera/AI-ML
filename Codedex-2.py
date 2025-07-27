# 17. Enter PIN

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')


# 18. Guess Number
# Write code below 💖

guess = 0
tries = 0

while guess != 6 and tries<5:
  guess = int(input("Guess the number:  "))
  tries = tries + 1

if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')



# 19. Detention 

for i in range(101):
  print(i , "I will not use Snapchat in class")


# 20. 99 Bottles
# Write code below 💖

# String concatenation

for i in range(99,0,-1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  print(f'{i-1} bottles of beer on the wall')

# 21. Fizz Buzz
# Write code below 💖

for i in range(1,101):
  if(i%3==0 and i%5==0):
    print('FizzBuzz')
  elif(i%3==0):
    print('Fizz')
  elif(i%5==0):
    print('Buzz')
  else:
    print(i)


# coddex program
# # Fizz Buzz 🐝
# # Codédex

# for num in range(1, 101):
#   if num % 3 == 0 and num % 5 == 0:
#     print('FizzBuzz')
#   elif num % 3 == 0:
#     print('Fizz')
#   elif num % 5 == 0:
#     print('Buzz')
#   else:
#     print(num)


# 22. Grocery List

# Write code below 💖

grocery = ['🥚 Eggs','🥑 Avocados','🍪 Cookies','🌶 Hot Pepper Jam','🫐 Blueberries','🥦 Broccoli']
print(grocery)


import random
computer = random.randint(1,3)
print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
player = int(input("Pick Number..."))


if(player==1 and computer==3):
    print('You Choose ✊')
    print('CPU Choose ✌️')
    print('You Win..')
elif(player==1 and computer==2):
    print('You Choose ✊')
    print('CPU Choose ✋')
    print('CPU Win..')
elif(player==2 and computer==1):
    print('You Choose ✋')
    print('CPU Choose ✊')
    print('You Win..')
elif(player==2 and computer==3):
    print('You Choose ✋')
    print('CPU Choose ✌️')
    print('CPU Win..')
elif(player==3 and computer==2):
    print('You Choose ✌️')
    print('CPU Choose ✋')
    print('You Win..')
elif(player==3 and computer==1):
    print('You Choose ✌️')
    print('CPU Choose ✊')
    print('CPU Win..')
elif(computer==1 and player==1):
    print("It's a tie!")
elif(computer==2 and player==2):
    print("It's a tie!")
elif(computer==3 and  player==3):
    print("It's a tie!")
else:
    print("Give number in range of 1 to 3")
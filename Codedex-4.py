# 35. Bob's Burgers |

# Write code below 💖


class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = True

bobs_burgers=Restaurant()

bobs_burgers.name='Bob\'s Burgers'
bobs_burgers.category='American Diner'
bobs_burgers.rating=4.7
bobs_burgers.delivery=False

print(vars(bobs_burgers))

# codeddex github

# Bob's Burgers 🍔
# Codédex

class Restaurant:
  name = ''
  type = ''
  rating = 0.0
  delivery = False

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.type = 'American Diner'
bobs_burgers.rating = 4.2
bobs_burgers.delivery = False

katz_deli = Restaurant()
katz_deli.name = 'Katz\'s Deli'
katz_deli.type = 'Kosher Deli'
katz_deli.rating = 4.5
katz_deli.delivery = True

baekjeong = Restaurant()
baekjeong.name = 'Baekjeong NYC'
baekjeong.type = 'Korean BBQ'
baekjeong.rating = 4.4
baekjeong.delivery = False

print(vars(bobs_burgers))
print(vars(katz_deli))
print(vars(baekjeong))


# 36. Favorite Cities

# Write code below 💖

class City:
  def __init__(self,name,country,population,landmark):
    self.name = name
    self.country=country
    self.population=population
    self.landmark=landmark

Dadar = City('dadar','gujrat',500,'near datar shop')
London = City('London','UK','9 million','Located on the River Thames, England')


print(vars(Dadar))
print(vars(London))


# CODEDEX GITHUB
# Favorite Cities 🏙️ 
# Codédex

class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks


nyc = City("New York City", "USA", 8468000, ["Statue of Liberty", "Brooklyn Bridge", "Apollo Theatre"])

shanghai = City("Shanghai", "China", 26320000, ["The Bund", "Jin Mao Tower", "Tianzifang"])

print(vars(nyc))
print(vars(shanghai))

# 37. Bank Accounts

# Write code below 💖

class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name=first_name
    self.last_name=last_name
    self.account_id=account_id
    self.account_type=account_type
    self.pin=pin
    self.balance=balance
  
  def deposit(self,add_money):
    self.balance=self.balance+add_money
    print("New Balance is ",self.balance)
  
  def withdraw(self,withdraw_money):
    self.balance=self.balance-withdraw_money
    print("New Balance is ",self.balance)

  def display_balance(self):
    print('Total Balance is ',self.balance)

Shubham=BankAccount('Shubham','Gajera',1,'Saving',1234,120.25)
Shubham.deposit(120)
Shubham.display_balance()
Shubham.withdraw(120)
Shubham.display_balance()
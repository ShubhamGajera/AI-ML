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



# 38. Pokédex

# Write code below 💖

class Pokemon:
  def __init__ (self,entry,name,types,description,is_caught,level,region,height,weight):
    self.entry=entry
    self.name=name
    self.types=types
    self.description=description
    self.is_caught=is_caught
    self.level=level
    self.region=region
    self.height=height
    self.weight=weight

  def speak(self):
    print(self.name*2)
  
  def display_details(self):
    print('Entry Number :',self.entry)
    print('Name:',self.name)
    print('Type:',self.types)
    print('Description:',self.description)
    print('Caught :',self.is_caught)
    print('Level :',self.level)
    print('Region :',self.region)
    print('Height :',self.height)
    print('Weight',self.weight)

Pikachu = Pokemon(25,'Pikachu','Electric','It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs. Pikachu has already been caught!','Yes',32,'Kanto','o.4 m','6 kg')
Pikachu.speak()
Pikachu.display_details()


# codedex github

# Pokédex 📟
# Codédex

# Class definition
class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(self.name + ', ' + self.name + '!')
  
  def display_details(self):
    print('Entry Number: ' + str(self.entry))
    print('Name: ' + self.name)

    if len(self.types) == 1:
      print('Type: ' + self.types[0])
    else:
      print('Type: ' + self.types[0] + '/' + self.types[1])
    
    print('Description: ' + self.description)

    if self.is_caught:
      print(self.name + ' has already been caught!')
    else:
      print(self.name + ' hasn\'t been caught yet.')

# Pokémon objects
pikachu = Pokemon(25, 'Pikachu', ['Electric'], 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', True)
charizard = Pokemon(6, 'Charizard', ['Fire', 'Flying'], 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', False)
gyarados = Pokemon(130, 'Gyarados', ['Water', 'Flying'], 'It has an extremely aggressive nature. The HYPER BEAM it shoots from its mouth totally incinerates all targets.', False)

pikachu.speak()
charizard.speak()
gyarados.speak()

# -----------------------------------------2

# Pokédex 📟
# Codédex

# Class definition
class Pokemon:
  def __init__(self, entry, name, types, description, level, region, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.level = level
    self.region = region
    self.is_caught = is_caught

  def speak(self):
    print(self.name + ', ' + self.name + '!')
  
  def display_details(self):
    print('Entry Number: ' + str(self.entry))
    print('Name: ' + self.name)

    if len(self.types) == 1:
      print('Type: ' + self.types[0])
    else:
      print('Type: ' + self.types[0] + '/' + self.types[1])
    
    print('Lv. ' + str(self.level))
    print('Region: ' + self.region)
    print('Description: ' + self.description)

    if self.is_caught:
      print(self.name + ' has already been caught!')
    else:
      print(self.name + ' hasn\'t been caught yet.')

# Pokémon objects
pikachu = Pokemon(25, 'Pikachu', ['Electric'], 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', 25, 'Kanto', True)
charizard = Pokemon(6, 'Charizard', ['Fire', 'Flying'], 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', 36, 'Kanto', False)
gyarados = Pokemon(130, 'Gyarados', ['Water', 'Flying'], 'It has an extremely aggressive nature. The HYPER BEAM it shoots from its mouth totally incinerates all targets.', 57, 'Kanto', False)

pikachu.speak()
charizard.speak()
gyarados.speak()
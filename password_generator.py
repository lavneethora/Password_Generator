import random
from lists import letters
from lists import numbers
from lists import symbols

password_generator_logo = """
  _____                                    _    _____                           _             
 |  __ \                                  | |  / ____|                         | |            
 | |__) |_ _ ___ _____      _____  _ __ __| | | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|                                                                                        
"""

print(password_generator_logo)    
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))
    
#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ""

for char in range(1, nr_letters + 1 ):
    l = random.choice(letters)
    easy_password += l
    
for char in range(1, nr_numbers + 1):
    n = random.choice(numbers)
    easy_password += n
    
for char in range(1, nr_symbols + 1):
    s = random.choice(symbols)
    easy_password += s

print("Your easy password is: ", easy_password)

#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

hard_password = ""
for char in password_list:
    hard_password += char
  
print("Your hard password is: ", hard_password)

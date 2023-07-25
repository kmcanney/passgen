#Password Generator Project
from replit import clear
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "_", "-"]

runagain = True
print("Welcome to Kevin's PyPassword Generator!\n(courtesy of '100 Days of Code: The Complete Python Pro Bootcamp for 2023')\n ")
while runagain == True:
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols?\n"))
  nr_numbers = int(input(f"How many numbers?\n"))
  
  
  password_list = []
  
  for letter in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
  
  for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
  
  for symbol in range(1, nr_symbols +1):
    password_list.append(random.choice(symbols))
  
  random.shuffle(password_list)
  
  password = ""
  
  for char in password_list:
    password += char
  
  print(f"You're not going to memorize this one, so copy and paste it into your favorite password manager:\n{password}")  

  repeat = input("Would you like to create another password? Press 'y' or 'n':  ").lower()

  if repeat == "y":
    runagain = True
    clear()
  else:
    runagain = False

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("!!!Remember if you won't answer for the last question (or answer something beside 's' or 'r') program will run automaticaly in standart order!!!")

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
order = str(input("Do you want your password in a standard order(letters->symbols->numbers) or random order? ('s'-standard; 'r'-random)\n").lower())

password_elements = []

for l in range(1,(nr_letters+1)):
      l =random.choice(letters)
      password_elements.append(l)
      
for s in range(1,(nr_symbols+1)):
      s = random.choice(symbols)
      password_elements.append(s)
      
for n in range(1,nr_numbers+1):
      n=random.choice(numbers)
      password_elements.append(n)

if order == "r":
      random.shuffle(password_elements)
      
password = "".join(password_elements)
print(f"Your password is: {password}")

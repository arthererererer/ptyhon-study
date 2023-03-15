#密碼設計1.
import itertools
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
a=[]
for let in range(0,nr_letters):
    a.append(random.choice(letters))
b=[]
for sym in range(0,nr_symbols):
    b.append(random.choice(symbols))
c=[]
for num in range(0,nr_numbers):
    c.append(random.choice(numbers))
d = list(itertools.chain(a,b,c)) 
random.shuffle(d)
password=""
for i in d:
    password=password+str(i)
print(password)
#密碼設計2.
password_list = []
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
  password += char
print(f"Your password is: {password}")
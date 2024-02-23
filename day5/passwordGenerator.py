#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#this is alternative method

# letter=random.sample(letters,nr_letters)
# letter_m=''.join(letter) 
# number=random.sample(numbers,nr_numbers)
# number_m=''.join(number)
# symbol=random.sample(symbols,nr_symbols)
# symbol_m=''.join(symbol)

# # print(f"the password generated is: {symbol_m}{letter_m}{number_m}")
# password=letter_m+number_m+symbol_m
# password_list=list(password)
# random.shuffle(password_list)
# print("the password generated is: ",''.join(password_list))


#this method uses the for loop
password=""
for char in range(1,nr_letters+1):
    random_letters=random.choice(letters)
    password+=random_letters


for num in range(1,nr_numbers+1):
    random_number=random.choice(numbers)
    password+=random_number

for sym in range(1,nr_symbols+1):
    random_symbol=random.choice(symbols)
    password+=random_symbol

password_list=list(password)
random.shuffle(password_list)
print("the password generated is :",''.join(password_list))









#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
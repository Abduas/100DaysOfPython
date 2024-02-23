import random
names_string=input("Give me everybody's names, separated by a comma and a space. ")
names = names_string.split(", ")
random_element=random.randrange(len(names))
random_name=names[random_element]
print(f"{random_name} is going to buy the meal today!")
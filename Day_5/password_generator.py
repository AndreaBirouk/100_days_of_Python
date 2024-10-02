import string
import random

# create a list for letters, numbers and special characters
# input from user for number of each element
# pick randomly certain number of elemenets from lists
# add these elements to a new list
# return them as a password in random order

alphabet_list = list(string.ascii_lowercase + string.ascii_uppercase)
numbers = list(string.digits)
characters = list(string.punctuation)


print('Welcome to my PyPassword Generator!')

nr_letters= int(input('How many letters would you like in your password \n'))
nr_numbers = int(input('How many numbers would you like? \n'))
nr_characters = int(input('How many special characters would you like? \n'))


random_letters = random.choices(alphabet_list, k=nr_letters)
random_numbers = random.choices(numbers, k= nr_numbers)
random_char = random.choices(characters, k=nr_characters)

random_elements = random_letters + random_numbers + random_char

password_list = random.choices(random_elements, k=len(random_elements))
password = ''.join(password_list)

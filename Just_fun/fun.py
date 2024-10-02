def find_love(name1, name2):
    total1 = 0
    total2 = 0
    names = [name1, name2]

    for letter in names:
        for char in letter:
            if char in 'tTrRuU':
                total1 += 1
            elif char in 'lLoOvV':
                total2 += 1
            elif char in 'eE':
                total1 += 1
                total2 += 1

    love_score = str(total1) + str(total2)
    return love_score

find_love("Kanye West", "Kim Kardashian")

'''
FizzBuzz
You are going to write a program that automatically prints the solution to the FizzBuzz game. 

These are the rules of the FizzBuzz game:

- Your program should print each number from 1 to 100 in turn and include number 100.

- But when the number is divisible by 3 then instead of printing the number it should print "Fizz".

- When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

'''
Write a program that returns True or False whether if a given year is a leap year.

This is how you work out whether if a particular year is a leap year. 
- on every year that is divisible by 4 with no remainder
- except every year that is evenly divisible by 100 with no remainder 
- unless the year is also divisible by 400 with no remainder   
'''


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False
    
# #option 1
# def add_cats(num):
#     word_list = []
#     for _ in range(num):
#         word_list.append('cats')
    

# #option 2
# def add_cats_alt(num):
#     word_list = ['cats'] * num
    


# add_cats(0)
# add_cats_alt(0)

# lines = [
#   "My King,",
#   "I need another five years.",
#   "Then your crab will be ready.",
#   "Sincerely,",
#   "Chuang-tzu"
# ]

# another_text = "\n".join(lines)



# def ArrayChallenge(strArr):
#     difference = 0
#     length = len(strArr[0])
#     for i in range(length):
#         if strArr[0][i] == strArr[1][i]:
#             difference += 0
#         else:
#             difference +=1

# ArrayChallenge(['10011', '10100'])
# import math
# def challenge(num):
#     hour = math.floor(num/60)
#     minute = (num - (hour * 60))
#     return f'{hour}:{minute}'

# print(challenge(45))

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }

# print(order['main'][2][0])

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)
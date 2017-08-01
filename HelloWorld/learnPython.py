# print('Welcome to the Pig Latin Translator!')
#
# pyg = "ay"
#
# original = input("Enter a word: ")
#
# if len(original) > 0 and original.isalpha():
#     word = original.lower()
#     first = word[0]
#     new_word = word + first + pyg
#     new_word = new_word[1:len(new_word)]
#     print(new_word)
# else:
#     print("empty")
# ============================================================


# def spam():
#     """This is a comment"""
#     print("Eggs!")
#
# spam()

#
# def power(base, exponent):  # Add your parameters here!
#     result = base**exponent
#     print ("%d to the power of %d is %d." % (base, exponent, result))
#
# power(37,4)

# from math import *
#
#
# def cube(number):
#     return pow(number, 3)
#
#
# def by_three(number):
#     if number % 3 == 0:
#         return cube(number)
#     else:
#         return False
#
#
# print(cube(3))
#
# print(sqrt(25))

# maximun = max(123, 1231, 3213)
# minimum = min(-8, -10, 5)
# absolute = abs(-42)
#
# print(maximun)
# print(minimum)
# print(absolute)
#
# print(type(84))
# print(type(53.5))
# print(type('spamsa'))

# def shut_down(s):
#     if s == 'yes':
#         return 'Shutting down'
#     elif s == 'no':
#         return 'Shutdown aborted'
#     else:
#         return 'Sorry'

# def distance_from_zero(arg):
#     if type(arg) == int or type(arg) == float:
#         return abs(arg)
#     else:
#         return 'Nope'
#
#
# def answer():
#     return 42
#
#
# def hotel_cost(nights):
#     return nights * 140
#
#
# def plane_ride_cost(city):
#     if city == 'Charlotte':
#         return 183
#     elif city == 'Tampa':
#         return 220
#     elif city == 'Pittsburgh':
#         return 222
#     elif city == 'Los Angeles':
#         return 475
#
#
# def rental_car_cost(days):
#     rent = days * 40
#     if days >= 7:
#         rent -= 50
#     elif days >= 3:
#         rent -= 20
#
#     return rent
#
#
# def trip_cost(city, days, spending_money):
#     return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
#
#
# print(trip_cost("Los Angeles",5,600))


##List
# zoo_animals = ["pangolin", "cassowary", "sloth", "Holi"];
# # One animal is missing!
#
# if len(zoo_animals) > 3:
#     print("The first animal at the zoo is the " + zoo_animals[0])
#     print("The second animal at the zoo is the " + zoo_animals[1])
#     print("The third animal at the zoo is the " + zoo_animals[2])
#     print("The fourth animal at the zoo is the " + zoo_animals[3])
#
#
# numbers = [5, 6, 7, 8]
#
# print( "Adding the numbers at indices 0 and 2...")
# print(numbers[0] + numbers[2])
# print("Adding the numbers at indices 1 and 3...")
# print(numbers[1] + numbers[3])
#
# suitcase = []
# suitcase.append("sunglasses")
#
# # Your code here!
# suitcase.append("ho")
# suitcase.append("li")
# suitcase.append("tas")
#
# list_length = len(suitcase)  # Set this to the length of suitcase
#
# print("There are %d items in the suitcase." % (list_length))
# print(suitcase)
#
# suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
#
# first = suitcase[0:2]  # The first and second items (index zero and one)
# middle = suitcase[2:4]  # Third and fourth items (index two and three)
# last = suitcase[4:6]  # The last two items (index four and five)


# animals = "catdogfrog"
# cat = animals[:3]  # The first three characters of animals
# dog = animals[3:6]  # The fourth through sixth characters
# frog = animals[6:]  # From the seventh character to the end


# animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
# duck_index = animals.index("duck")
#
# # Your code here!
# animals.insert(duck_index, "cobra")
#
# print(animals)  # Observe what prints after the insert operation

# my_list = [1,9,3,8,5,7]
#
# for number in my_list:
#     print(number * 2)

# backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
#
# backpack.remove('dagger')


# start_list = [5, 3, 1, 2, 4]
# square_list = []
#
# for number in start_list:
#     square_list.append(number**2)
#
# square_list.sort()
#
# print (square_list)

# Dictionary
# residents = {'Puffin': 104, 'Sloth': 105, 'Burmese Python': 106}
#
# print(residents['Puffin'])
# print(residents['Sloth'])
# print(residents['Burmese Python'])
#
# menu = {'Chicken Alfredo': 14.50}  # Empty dictionary
# print(menu['Chicken Alfredo'])
#
# # Your code here: Add some dish-price pairs to menu!
# menu['Paisana'] = 15.65
# menu['Paisana2'] = 15.65
# menu['Paisana3'] = 15.65
#
# print("There are " + str(len(menu)) + " items on the menu.")
# print(menu)

# key - animal_name : value - location
# zoo_animals = {'Unicorn': 'Cotton Candy House',
#                'Sloth': 'Rainforest Exhibit',
#                'Bengal Tiger': 'Jungle House',
#                'Atlantic Puffin': 'Arctic Exhibit',
#                'Rockhopper Penguin': 'Arctic Exhibit'}
# # A dictionary (or list) declaration may break across multiple lines
#
# # Removing the 'Unicorn' entry
# del zoo_animals['Unicorn']
# del zoo_animals['Sloth']
# del zoo_animals['Bengal Tiger']
#
# zoo_animals['Rockhopper Penguin'] = 'AA'
#
# print(zoo_animals)
#
# inventory = {
#     'gold' : 500,
#     'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
#     'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# }
#
# # Adding a key 'burlap bag' and assigning a list to it
# inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
#
# # Sorting the list found under the key 'pouch'
# inventory['pouch'].sort()
#
# # Your code here
# inventory['pocket'] = ['seashell','strange berry','lint']
#
# inventory['backpack'].sort()
#
# inventory['backpack'].remove('dagger')
#
# inventory['gold'] = inventory['gold'] + 50
#
# print(inventory)


# Loops
# names = ["Adam", "Alex", "Mariah", "Martine", "Columbus"]
#
# for name in names:
#     print(name)

# webster = {
#     "Aardvark": "A star of a popular children's cartoon show.",
#     "Baa": "The sound a goat makes.",
#     "Carpet": "Goes on the floor.",
#     "Dab": "A small amount."
# }
#
# for key in webster:
#     print(webster[key])
#
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# for num in a:
#     if num % 2 == 0:
#         print(num)
#
# def fizz_count(x):
#     count = 0
#
#     for item in x:
#         if item == 'fizz':
#             count += 1
#
#     return count
#
# array = ["fizz", "cat", "fizz"]
# print(fizz_count(array))

# shopping_list = ["banana", "orange", "apple"]
#
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
#
#
# def compute_bill(food):
#     total = 0
#
#     for f in food:
#         if stock[f] > 0:
#             total += prices[f]
#             stock[f] -= 1
#
#     return total

# for key in prices:
#     print(key)
#     print("price: %s" % prices[key])
#     print("stock: %s" % stock[key])
#
# total = 0
#
# for key in prices:
#     earning = prices[key] * stock[key]
#     print(earning)
#     total += earning
#
# print(total)

# Review
# lloyd = {
#     'name': "Lloyd",
#     'homework': [90.0, 97.0, 75.0, 92.0],
#     'quizzes': [88.0, 40.0, 94.0],
#     'tests': [75.0, 90.0]
# }
# alice = {
#     "name": "Alice",
#     "homework": [100.0, 92.0, 98.0, 100.0],
#     "quizzes": [82.0, 83.0, 91.0],
#     "tests": [89.0, 97.0]
# }
# tyler = {
#     "name": "Tyler",
#     "homework": [0.0, 87.0, 75.0, 22.0],
#     "quizzes": [0.0, 75.0, 78.0],
#     "tests": [100.0, 100.0]
# }
# students = [
#     lloyd, alice, tyler
# ]


# for student in students:
#     print(student['name'])
#     print(student['homework'])
#     print(student['quizzes'])
#     print(student['tests'])


# def average(numbers):
#     total = sum(numbers)
#     return float(total) / len(numbers)
#
#
# def get_average(student):
#     homework = average(student['homework'])
#     quizzes = average(student['quizzes'])
#     tests = average(student['tests'])
#
#     return 0.1 * homework + 0.3 * quizzes + 0.6 * tests
#
#
# def get_letter_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"
#
#
# def get_class_average(students):
#     results = []
#     for stu in students:
#         results.append(get_average(stu))
#
#     return average(results)
#
# print(get_class_average(students))
# print(get_letter_grade(get_class_average(students)))


# n = [1, 3, 5]
# n[1] = n[1] * 5
# n.append(4)
# n.remove(1)
# print(n)


def string_function(s):
    return s + 'world'


# BattleShip
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print("Turn", turn + 1)

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    print(ship_col)
    print(ship_row)

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
    else:
        if guess_row not in range(5) or \
                        guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

        print_board(board)

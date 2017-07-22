# python

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

webster = {
    "Aardvark": "A star of a popular children's cartoon show.",
    "Baa": "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for key in webster:
    print(webster[key])

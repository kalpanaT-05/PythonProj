fruits = ["oranges", "apples", "grapes", "banana", "apples", "apples", "apples", "apples"]
number = [1, 52, 1997, 345.89, 1990]

# fruits.append("litchie")
# print(fruits)

# number.append(2)
# print(number)

# fruits.extend(number)
# print(fruits)

"""remove() method is used if we want to remove an item from the list with the exact match of the name"""
# fruits.remove("grapes")
# print(fruits)

"""pop() method can be used by using index of an items to remove an items from the list"""
# fruits.pop(1)
# print(fruits)

"""if we want to remove an items from the end then we can use negative index number with pop() method to remove an item from the list"""
# number.pop(-1)
# print(number)
#
# number.sort()
# print(number)

"""in function used for searching an item in the list"""
print("apple" in fruits)
print("apples" in fruits)

"""count() method used for counting the total items of the exact match in the list"""
print(fruits.count("apples"))
fruits.append("apples")
print(fruits.count("apples"))

"""index() method gives index position of an instance it finds at the first place"""
print(fruits.index("apples"))
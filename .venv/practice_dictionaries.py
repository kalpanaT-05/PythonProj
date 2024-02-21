stuff = {"food": 12, "energy": 100, "enemies": 3}

"""get() method is used to get the value of the key"""
# print(stuff.get("food"))

"""items() method used to return the items in order"""
# print(stuff.items())

"""keys() method returns all of the keys in the dictionary"""
# print(stuff.keys())

"""popitem() method used to remove item from the last from the dictionary"""
# print(stuff.popitem())
# print(stuff)

"""setdefault() method used to set any value to default"""
# print(stuff.setdefault("food"))
# print(stuff)
# print(stuff.setdefault("friends", 123))
# print(stuff)

new_items = {"rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

new_items = {"rocks": 5, "webs": 5}
stuff.update(new_items)
print(stuff)

up_items = {"food": 3, "friend": 1}
stuff.update(up_items)
print(stuff)

stuff.update(food = 20, cake = 10)
print(stuff)
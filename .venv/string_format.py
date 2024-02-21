"""data types - String"""
name = "Jessica Jones"
type_of_car = "Sedan"
school = "Foundation Elementary School"

"""first type of string format printing"""
print(name + school)

"""second type using double quotes for space while printing"""
print(name + " " + school)

"""a little improved way of writing code and saving time"""
print(name + " works at " + school + ".")

"""python format method/function using curly braces {} in place of variables to do things more efficiently"""
#python string.format()
print("{} works at {}.".format(name, school))
"""the format method or format function actually accepts the arguments of our
variables and transfers those arguments into the curly braces in the order
that they appear in the sentence."""
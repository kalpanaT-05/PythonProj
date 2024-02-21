# def user(name, age, city):
#     '''this function prints name, age and city from an argument
#     provided to the function.'''
    # print("{} is {} years old, from {}.".format(name, age, city))
# user("Jane", 50, "Rome")

# keyword arguments
# def user_info(name1, age1=0, city1="Michigan"):
#     print("{} is {} years old, from {}.".format(name1, age1, city1))
# user_info("Jane")

# *args : any number of positional arguments
def add(*integers):
    print(sum(integers))
add(25, 30, 45, 50)
add(23.5, 26, 48.980)
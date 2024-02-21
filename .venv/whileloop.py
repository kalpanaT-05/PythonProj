temp = 40

while temp > 32:
    print("Temperature is {}".format(temp))
    temp = temp - 1
    if temp == 33:
        break

for i in range(1,10):
    if i == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}.".format(i))

for i in range(1,9):
    if i == 3:
        pass
    else:
        print("This number is {}.".format(i))
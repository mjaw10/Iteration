multiplyer = 1
number = int(input("Please enter an integer: "))
print("Times table for {0}".format(number))
for count in range(12):
    answer = multiplyer * number
    print("{0} * {1} = {2}".format(multiplyer,number,answer))
    multiplyer = multiplyer + 1

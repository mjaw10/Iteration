# program to prompt for 8 numbers and report the total to the user
num = 0
for count in range(8):
    num = num + int(input("Enter a number: "))
print("The total is {0}".format(num))

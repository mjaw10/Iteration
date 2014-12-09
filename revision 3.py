#Matthew Wadkin
#16/10/14

num = int(input("How many numbers are ther to be averaged?\n"))
num1 = 0
for count in range(num):
    num1 = num1 + float(input("Enter a number:\n"))
average = num1 / num
print("The average of those numbers is {0}".format(average))

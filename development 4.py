#Matthew Wadkin
#16/10/14

num = int(input("Please enter a number: "))
num_1 = 1                
while num_1 > 0:
    num_1 = int(input("Please enter another number (or -1 to stop entering numbers): "))
    if num_1 > num:
        num = num_1
print("The highest number you entered is {0}".format(num))

#Matthew Wadkin
#22/10/2014
number = int(input("Please enter the number you want to square up to: "))
output = " "
while number > 0:
    square = number * number
    
    output = str(square) + " " + str(output)
    number = number - 1
print(square)

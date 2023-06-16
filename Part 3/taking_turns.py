# Write your solution here
number = int(input("Please type in a number:"))
integer = 1
while True:
    if number < integer:        
        break
    elif integer < number:
        print(integer)
        print(number)
    else:
        print(integer)
    integer += 1
    number -= 1
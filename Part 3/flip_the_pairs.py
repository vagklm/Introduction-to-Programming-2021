# Write your solution here
number = int(input("Please type in a number:"))
integer = 1
while True:
    if integer > number:
        break
    elif integer < number:
        print(integer+1)
        print(integer)
    else:
        print(integer)
    integer += 2

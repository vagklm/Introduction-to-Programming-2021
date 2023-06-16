# Write your solution here
string = input("Please type in a string:")
print(string[len(string)-1])
number = len(string)-2
while number >= 0:
    print(string[number:len(string)-1]+string[len(string)-1])
    number -= 1
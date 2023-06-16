# Write your solution here
string = input("Please type in a string:")
print(string[0])
number = 2
while number <= len(string):
    print(string[0:number])
    number += 1
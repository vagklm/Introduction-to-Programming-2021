# Write your solution here
string = input("Please type in a string:")
char = input("Please type in a char:")
index = string.find(char)
if index >= 0 and index +2 < len(string):
    print(string[index:index+3])

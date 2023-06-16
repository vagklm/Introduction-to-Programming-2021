# Write your solution here
string = input("Please type in a string:")
char = input("Please type in a char:")
while True:
    index = string.find(char)
    if len(string) == 0:
        break
    if index >= 0 and index +2 < len(string):
        print(string[index:index+3])
        if char == string[index+1]:
            print(string[index+1:index+4])
    string = string[index+2:]

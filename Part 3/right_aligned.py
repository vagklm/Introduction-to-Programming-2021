# Write your solution here
string = input("Please type in a string:")
if len(string) == 20:
    print(string)
elif len(string) < 20:
    print("*"*(20-len(string))+string)

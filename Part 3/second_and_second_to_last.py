# Write your solution here
string = input("Please type in as string:")
if string[1] == string[len(string)-2]:
    print(f"The second and the second to last characters are {string[1]}")
else:
    print("The second and the second to last characters are different")

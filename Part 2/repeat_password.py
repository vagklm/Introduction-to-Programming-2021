# Write your solution here
password = input("Password:")
while True:
    verify = input("Repeat password:")
    if password != verify:
        print("They do not match!")
    else:
        break
print("User account created!")
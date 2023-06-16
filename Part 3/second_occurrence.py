# Write your solution here
string = input('Please type in a string:')
substring = input("Please type in a substring:")
index = string.find(substring)
if index >= 0 and index + 2 < len(string) and len(string) >3:
    index1 = string[index+1:len(string)].find(substring)     
    if index1 >=0 and not(substring in string[index+index1+1:index+index1+3]):
        print(f"The second occurrence of the substring is at index {index1+index+1}.")
    elif index1 >= 0 and substring in string[index+index1+1:index+index1+3]:
        index2 = string[index+index1+2:len(string)].find(substring)
        print(f"The second occurrence of the substring is at index {index1+index+index2+2}.")
    else:
        print("The substring does not occur twice in the string.") 
if index >= 0 and len(string) <= 3:
    index1 = string[index+1:len(string)].find(substring)
    if index1 >=0:
        print(f"The second occurrence of the substring is at index {index1+index+1}.")
    else:
       print("The substring does not occur twice in the string.") 
if index < 0:
    print("The substring does not occur twice in the string.") 


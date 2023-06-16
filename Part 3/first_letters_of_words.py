# Write your solution here
sentence = input("Please type in a sentence:")
print(sentence[0])
while True:
    index = sentence.find(" ")
    if index < 0:
        break
    print(sentence[index+1])
    sentence = sentence[index+2:]

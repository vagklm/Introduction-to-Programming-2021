# Write your solution here
words = ""
nwords = 0
previousword = ""
while True:
    word = input("Please type in a word:")
    nwords += 1
    if word == previousword and word != "end":
        print(words)
        break
    if word != "end" and word != previousword:
        words += word + " "
        previousword = word
    if word == "end" and nwords == 1:
        break
    if word == "end" and nwords > 1:
        print(words)
        break
    
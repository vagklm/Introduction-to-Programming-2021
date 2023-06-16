# Write your solution here
word = input("Word:")
print("*"*30)
if len(word) % 2 == 0:
    print("*"+" "*((28-len(word))//2)+word+" "*((28-len(word))//2)+"*")
else:
    print("*"+" "*((28-len(word)-1)//2)+word+" "*((28-len(word)+1)//2)+"*")
print("*"*30)
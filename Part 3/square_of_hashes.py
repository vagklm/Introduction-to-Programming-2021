# Write your solution here
def hash_square(length):
    number = 1
    while number <= length:
        print("#"*length)
        number +=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(6)
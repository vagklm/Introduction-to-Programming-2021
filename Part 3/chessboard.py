# Write your solution here
def chessboard(x):
    number1 = 0
    number2 = 0
    while number1 <= x-1:
        if number1 % 2 != 0:
            for number2 in range(x):
                if number2 % 2 == 0:
                    print(0,end="")
                else:
                    print(1,end="")
                number2 +=1
        else:
            for number2 in range(x):
                if number2 % 2 ==0:
                    print(1,end="")
                else:
                    print(0,end="")
                number2 +=1
        number1 += 1
        print('')


# Testing the function
if __name__ == "__main__":
    chessboard(6)

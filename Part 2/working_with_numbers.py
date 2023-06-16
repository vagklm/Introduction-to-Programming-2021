# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
print("...the program asks for numbers")
numbers = 0
sumar = 0
positives = 0
negatives = 0
while True:
    number = int(input("Number:"))
    numbers += 1
    sumar += number
    if number > 0:
        positives += 1
    if number < 0:
        negatives += 1
    if number == 0:
        print(f"Numbers typed in {numbers-1}")
        print(f"The sum of the numbers is {sumar-number}")
        print(f"The mean of the numbers is {(sumar-number)/(numbers-1)}")
        print(f"Positive numbers {positives}")
        print(f"Negative numbers {negatives}")
        break
    
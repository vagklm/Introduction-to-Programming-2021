number = int(input("Please type in a number:"))
op1 = 1
while True:
    if op1 > number:
        break
    op2 = 1
    while op2 <= number:
        print(f"{op1} x {op2} = {op1*op2}")
        op2 += 1
    op1 += 1



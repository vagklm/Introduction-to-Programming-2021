# Write your solution here
gift = int(input("Value of gift:"))
if gift < 5000:
    print("No tax!")
elif 5000 <= gift < 25000:
    print(f"Amount of tax: {100+(gift-5000)*0.08}")
elif 25000 <= gift < 55000:
    print(f"Amount of tax: {1700+(gift-25000)*0.1}")
elif 55000 <= gift < 200000:
    print(f"Amount of tax: {4700+(gift-55000)*0.12}")
elif 200000 <= gift <1000000:
    print(f"Amount of tax: {22100+(gift-200000)*0.15}")
elif gift >= 1000000:
    print(f"Amount of tax: {142100+(gift-1000000)*0.17}")
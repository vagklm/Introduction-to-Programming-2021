# Write your solution here
year = int(input("Please type in a year:"))
year2 = year + 1
while True:
    if year2 % 4 == 0 and year2 % 100 == 0 and year2 % 400 == 0:
        print(f"The next leap year after {year} is {year2}")
        break
    if year2 % 4 == 0 and year2 % 100 != 0:
        print(f"The next leap year after {year} is {year2}")
        break
    year2 += 1

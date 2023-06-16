# Write your solution here
hwage = float(input("Hourly wage:"))
hwork = float(input("Hours worked:"))
day = input("Day of the week:")
dwage = hwage*hwork
if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday"):
    print(f"Daily wages: {dwage} euros")
if day == "Sunday":
    print(f"Daily wages: {dwage*2} euros")

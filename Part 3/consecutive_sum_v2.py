# Write your solution here
limit = int(input("Limit:"))
sumar = 0
number = 0
nstring = ""
while sumar < limit:
    number += 1
    sumar += number
    if sumar >= limit:
        nstring += f"{number}"
    if sumar < limit:
        nstring += f"{number} + "
print(f"The consecutive sum: {nstring} = {sumar}")
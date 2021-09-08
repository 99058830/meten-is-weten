print("Geef twee getallen")
a = input("Voer uw eerste getal in. ")
b = input("Voer uw tweede getal in. ")

maximum = b
minimum = a

if a > b:
    print("a is het grootste getal")
elif a < b:
    print("a is het kleinste getal")
if a == b:
    print("a en b zijn even groot")

print("Het minimum is: ", minimum)
print("Het maximum is: ", maximum)
n = int(input("Enter the number:"))

if n % 3 == 0 and n % 5 == 0:
    print("Legend")
elif n % 3 == 0:
    print("Wizard")
elif n % 5 == 0:
    print("Devil")
else:
    print("Awww!")


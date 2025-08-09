n = int(input("Enter the number:"))

if n % 3 == 0 and n % 5 == 0 and n % 2 == 0:
    print("Legend")
elif n % 2 == 0:
    print("Wizard")
elif n % 3 == 0:
    print("Devil")
elif n % 5 == 0:
    print ("Code Monkey!")
else:
    print("Awww!")


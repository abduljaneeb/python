name = input("Enter your name: ")

age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name}, you are eligible for election")

if age < 18:
    print(f"{name}, you are not eligible for election")

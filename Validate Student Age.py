try:
    age = int(input("Enter Age: "))

    if age < 5 or age > 30:
        raise ValueError("Invalid Student Age")

    print("Accepted")

except ValueError as e:
    print(e)
gross = float(input("Enter gross salary: "))
tax = float(input("Enter tax percentage: "))

net = gross - (gross * tax / 100)

print("Net salary is:", net)
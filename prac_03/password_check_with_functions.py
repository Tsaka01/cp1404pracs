password = input("Enter a password: ")
if len(password) < 2:
    print("Invalid - password is too small")
    password = input("Enter a password: ")
if len(password) > 10:
    print("Invalid - password is too large")
    password = input("Enter a password: ")
print('*' * len(password))
print()
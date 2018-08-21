def main():
    password = get_password()
    show_password(password)


def get_password():
    password = input("Enter a password: ")
    if len(password) <= 3:
        print("Invalid - password is too small")
        password = input("Enter a password: ")
    if len(password) > 10:
        print("Invalid - password is too large")
        password = input("Enter a password: ")
    return password


def show_password(password):
    print('*' * len(password))
    print()


main()

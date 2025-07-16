from getpass import getpass
from termcolor import colored

def main() -> None:

    with open('data/users.txt') as f:
        users = []
        for line in f.readlines():
            username, password = line[:-1].split(', ')
            users.append({
                'username': username,
                'password': password
            })

    print("1. Kirish")
    print("2. Ro'yxatdan o'tish")

    op = input("> ")

    if op == '1':
        pass
    elif op == '2':
        username = input("username: ")
        password = getpass("password: ")
        confirm_password = getpass("confirm password: ")

        if password != confirm_password:
            print("parol mos emas.")
        elif username in list(map(lambda user: user['username'], users)):
            print("bu username tanlangan.")
        else:
            with open("data/users.txt", "a") as f:
                f.write(f"{username}, {password}\n")
    else:
        print("xato tanlov")

main()

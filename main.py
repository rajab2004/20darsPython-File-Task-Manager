from getpass import getpass
from printers import print_menu, print_satus


def main() -> None:

    with open('data/users.txt') as f:
        users = []
        for line in f.readlines():
            username, password = line[:-1].split(', ')
            users.append({
                'username': username,
                'password': password
            })

    print_menu()

    op = input("> ")

    if op == '1':
        pass
    elif op == '2':
        username = input("username: ")
        password = getpass("password: ")
        confirm_password = getpass("confirm password: ")

        if password != confirm_password:
            print_satus("parol mos emas.", 'error')
        elif username in list(map(lambda user: user['username'], users)):
            print_satus("bu username tanlangan.", "error")
        else:
            with open("data/users.txt", "a") as f:
                f.write(f"{username}, {password}\n")
            print_satus("ro'yxatdan otdingiz.", 'success')
    else:
        print("xato tanlov")

main()

from termcolor import colored

def menyuni_chiqarish():
    print("1. Kirish")
    print("2. Ro'yxatdan o'tish")

def holatni_chiqarish(matn, holat):
    ranglar = {
        'error': 'red',
        'success': 'green'
    }
    rangli_matn = colored(matn, ranglar[holat])
    print(rangli_matn)

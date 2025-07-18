from getpass import getpass
from printers import menyuni_chiqarish, holatni_chiqarish
from utils import (
    foydalanuvchi_yaroqli, parollar_mosmi, 
    parol_yaroqli, foydalanuvchilarni_yuklash, 
    foydalanuvchi_qoshish, parolni_shifrlash,
    login_bandmi, foydalanuvchini_ol,
)

def asosiy() -> None:
    menyuni_chiqarish()

    tanlov = input("> ")

    if tanlov == '1':
        login = input("Login: ")
        parol = getpass("Parol: ")

        foydalanuvchi = foydalanuvchini_ol(login, parol)
        if foydalanuvchi:
            holatni_chiqarish("Muvaffaqiyatli kirdingiz.", 'success')
        else:
            holatni_chiqarish("Foydalanuvchi topilmadi.", 'error')

    elif tanlov == '2':
        login = input("Login: ")
        parol = getpass("Parol: ")
        tasdiq_parol = getpass("Parolni tasdiqlang: ")

        if login_bandmi(login):
            holatni_chiqarish("Bu login band.", "error")
        elif not foydalanuvchi_yaroqli(login):
            holatni_chiqarish("Login faqat harflardan iborat bo'lishi kerak.", 'error')
        elif not parol_yaroqli(parol):
            holatni_chiqarish("Parol kamida 8 ta belgidan iborat bo'lishi kerak.", 'error')
        elif not parollar_mosmi(parol, tasdiq_parol):
            holatni_chiqarish("Parollar mos emas.", 'error')
        else:
            foydalanuvchi_qoshish(login, parolni_shifrlash(parol))
            holatni_chiqarish("Ro'yxatdan o'tdingiz.", 'success')
    else:
        print("Noto'g'ri tanlov.")

asosiy()

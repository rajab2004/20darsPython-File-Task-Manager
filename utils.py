from hashlib import sha256

def foydalanuvchi_yaroqli(login: str) -> bool:
    return login.isalpha()

def parol_yaroqli(parol: str) -> bool:
    return len(parol) >= 8

def parollar_mosmi(parol: str, tasdiq: str) -> bool:
    return parol == tasdiq

def foydalanuvchilarni_yuklash() -> list[dict]:
    with open('data/users.txt') as f:
        foydalanuvchilar = []
        for qator in f.readlines():
            login, parol = qator[:-1].split(', ')
            foydalanuvchilar.append({
                'login': login,
                'parol': parol
            })

    return foydalanuvchilar

def foydalanuvchi_qoshish(login: str, parol: str):
    with open("data/users.txt", "a") as f:
        f.write(f"{login}, {parol}\n")

def parolni_shifrlash(parol: str) -> str:
    shifrlangan = sha256(parol.encode()).hexdigest()
    return shifrlangan

def login_bandmi(login: str) -> bool:
    foydalanuvchilar = foydalanuvchilarni_yuklash()
    return login in list(map(lambda foy: foy['login'], foydalanuvchilar))

def foydalanuvchini_ol(login: str, parol: str) -> dict:
    foydalanuvchilar = foydalanuvchilarni_yuklash()
    shifrlangan = parolni_shifrlash(parol)

    for foy in foydalanuvchilar:
        if foy['login'] == login and foy['parol'] == shifrlangan:
            return foy
    
    return None

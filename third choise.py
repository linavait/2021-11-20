def mano_duomenys(vardas, pavarde, amzius):
    if amzius >= 100:
    result = "garbus"
    else:
        result = "jaunas"

    print(f"{vardas} {pavarde} {amzius} iki 100metu liko {100 - amzius}")

if __name__ == '__main__':
    tavo_amzius = input("koks tavo amzius ")
    tavo_vardas = input("koks tavo vardas ")
    tavo_pavarde = input("kokia tavo pavarde ")
    tavo_amzius = int(tavo_amzius)
    mano_duomenys(tavo_vardas, tavo_pavarde, tavo_amzius)


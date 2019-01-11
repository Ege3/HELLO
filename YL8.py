aasta = int(input("Sisesta aastaarv: "))
if aasta % 4 == 0 and aasta % 100 != 0 or aasta % 400 == 0:
    print("liigaasta")
else:
    print("lihtaasta")

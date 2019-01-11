nimi = input("Mis nimeks on? ").capitalize()
print("Tervitus " + nimi + "!")
elukoht = input("Kus " + nimi + " elab? ")
if "saaremaa" in elukoht.lower():
    print("Kena värk!")
vanus = int(input("Kui vana " + nimi + " on? "))
if vanus < 18:
    print(nimi + ", oled veel liiga noor, et autot juhtida.")
elif vanus == 18:
    print(nimi + ", õnnitlen täisealiseks saamise puhul!")
else:
    print(nimi + ", võid autot juhtida.")

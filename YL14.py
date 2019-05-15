#Leia muutuja abil etteantud tekstis olevate 
# täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv. 
jutt = input("sisesta tekst:")
taishaalikud = ["a", "e", "i","o", "u", "õ", "ä", "ö", "ü"]
tuleb = 0
for taht in jutt:
    if taht in taishaalikud:
        tuleb +=1
print(str(tuleb))
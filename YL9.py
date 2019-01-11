esimene = float(input("Sisesta kolmnurga esimene külg: "))
teine = float(input("Sisesta kolmnurga teine külg: "))
kolmas = float(input("Sisesta kolmnurga kolmas külg: "))

#kaks lühemat külge peavad kokku andma kõige pikema külje:
list = [esimene, teine, kolmas]
if (max(list)) == esimene and teine + kolmas >= (max(list)) or (max(list)) == teine and esimene + kolmas >= (max(list)) or (max(list)) == kolmas and teine + esimene >= (max(list)):
    if esimene == teine and esimene == kolmas:
        print("Tegemist on võrdkülgse kolmnurgaga")
    elif esimene == teine or esimene == kolmas or teine == kolmas:
        print("Tegemist on võrdhaarse kolmnurgaga")
    else:
        print("Tegemist on erikülgse kolmnurgaga")
else:
    print("Kolmnurka ei saa eksisteerida")

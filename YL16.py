#Arvu arvamise mäng. 
#Arvuti mõtleb välja arvu nullist sajani. Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
#Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. 
#Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)
import random
arvuti_arv = random.randint(0,100)
print(arvuti_arv) #arvu kontrolliks, et kas töötab
kasutaja_arv = int(input("Mis arvu pakud?: "))

while arvuti_arv > kasutaja_arv or arvuti_arv < kasutaja_arv:
    if arvuti_arv > kasutaja_arv:
        print("sinu arv on väiksem arvuti omast")
    elif arvuti_arv < kasutaja_arv:
        print("Sinu oma on suurem arvuti omast")
    kasutaja_arv = int(input("Mis arvu pakud?: "))
    if arvuti_arv == kasutaja_arv:
        break

if arvuti_arv == kasutaja_arv:
    print("õige vastus!")






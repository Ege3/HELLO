arv1 = int(input("sisesta arv 1: "))
arv2 = int(input("sisesta arv 2: "))
arv3 = int(input("sisesta arv 3: "))
if arv1 > arv2 and arv1 > arv3:
    print(arv1)
elif arv2 > arv1 and arv2 > arv3:
    print(arv2)
else:    
    print(arv3)

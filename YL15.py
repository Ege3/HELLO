#Väljasta korduslause abil 8 korrutis arvudega 0..12
    #8 x 0 = 0
	#8 x 1 = 8
	#8 x 2 = 16
	#…
	#8 x 12 = 96
#Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse
number = int(input("Sisesta number, millega soovid korrutada:"))
i = 0
while i <= 12:
    print(i*number)
    i = i + 1

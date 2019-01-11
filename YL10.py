puuvilja_list = ['pirn', 'kirss', 'ploom']
print(puuvilja_list[0])
puuvilja_list.insert(3,'apelsin')
print(puuvilja_list[3])
#print(puuvilja_list)
puuvilja_list[2] = 'õun'
print(puuvilja_list)
if "õun" in puuvilja_list:
  print("Jah, 'õun' on listis")
print(len(puuvilja_list))
del puuvilja_list[0]
print(puuvilja_list)
puuvilja_list.reverse()
print(puuvilja_list)
puuvilja_list.sort()
print(puuvilja_list)
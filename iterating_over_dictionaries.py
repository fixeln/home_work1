friend_ages = {"Rolf" : 25, "Anne" : 37, "Charlie" : 31, "Bob" : 22}

for name in friend_ages: #para buscar chaves
    print(name)
for age in friend_ages.values(): #para buscar valores das chaves
    print(age)

for name, age in friend_ages.items(): #mostra tudo
    print(f"{name} is {age} years old")

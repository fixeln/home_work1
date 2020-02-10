friends = ["Rolf", "Anne", "Rob", "Charlie", "Jen"]

print(friends[1:4]) #devolve tudo que se encontra entre inex 1 e 4 inclusive
print(friends[:1]) #devolve tudo ate ao index 1 inclusive
print(friends[2:]) #deolve tudo a partir do index 2 inclusive
print(friends[:]) #devolve a mesma lista quando se quer guardar na outra lista os valores
print(friends[-3:]) #devolve tudo da pasicação do fim 3 valores
print(friends[-3:-1]) # == print(friends[-3:4]) devole o mesmo menos o último


hello_1 = "Friends"
slice_instance = slice(0,4)
print(hello_1[slice_instance])

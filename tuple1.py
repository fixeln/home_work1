tuple1 = (1,2,3,4, 'string', 5, 5)
new_tuple = tuple()
for i in tuple1:
    if not isinstance(i,str):
        new_tuple += (i,)
print(new_tuple)

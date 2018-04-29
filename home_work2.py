
list1 = [ 1, 5, 5, 44, 21, 100]
list1.sort()
print (list1)

dict1 = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five'}
for i in dict1:
		print(i,dict1[i])

tupple1 = (1.2, 4.3, 1.0, 2.03, 50.3, 0.2, 3.4, 0.2, 4.0, 22.22)
print(max(tupple1), min(tupple1))

list2 = ['Earth', 'Portugal', 'Lisbon']
indx = 0
for l in list2:
	indx = indx + 1
	if indx != 3:
	    print(l,'-> ',end = '')
	else: 
	    print(l)

str = '/bin:/usr/bin:/usr/local/bin'
str2 = str.split(':')
print(str2)

ran1 = range(1,100,1)
for r in ran1:
	if ( r % 7 ) == 0:
		print( '{} Divided by 7 ' .format(r))
	else:
		print( '{} Not devided by 7' .format(r))
		

matrix = [[ 1, 2, 3],
		   [ 4, 5, 6 ],
		   [ 7, 8, 9 ],
		   [ 10, 11, 12 ]]
for row in matrix:
	print(row)
	for ele in row:
		print(ele)

list3 = ['Bella', 'ciao', 'oh', 'bella', 'ciao']
for inda,l2 in enumerate(list3):
	print (l2, inda)

list4 = ['to-delete', 4, 'to-delete', 'not-delete', 'to-not-delete', 'to-delete', 55]
while 'to-delete' in list4:
	list4.remove('to-delete')
print(list4)

list5 = range(10,0,-1)
for l5 in list5:
	print(l5)
		
		   
		    

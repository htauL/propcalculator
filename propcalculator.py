exit = False
print('This is the personal proportion calculator from htauL \n\n a/b = c/d \n\n Mode=discover one term.\n\n')
while exit == False:
	mode = input('Which term you want to find?\n\n[a]\n[b]\n[c]\n[d]\n\nChoose one(only c available): ').upper().strip()
	if mode == 'C':
		a = float(input('a = '))
		b = float(input('b = '))
		d = float(input('d = '))
		c = (a*d)/b
		print(f'c is equal to {c}')
	
	
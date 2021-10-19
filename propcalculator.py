exit = False
print('This is the personal proportion calculator from htauL \n\n a/b = c/d \n\n Mode = discover one term.\n\n')
while exit == False:
	term = input('Which term you want to find?\n\n[a]   [c]\n--- = ---\n[b]   [d]\n\nChoose one: ').upper().strip()
	if term == 'A':
		b = float(input('b = '))
		c = float(input('c = '))
		d = float(input('d = '))
		a = (b*c)/d
		print(f'{term} is equal to {a}\n')
		
	if term == 'B':
		a = float(input('a = '))
		c = float(input('c = '))
		d = float(input('d = '))
		b = (a*d)/c
		print(f'{term} is equal to {b}\n')
		
	if term == 'C':
		a = float(input('a = '))
		b = float(input('b = '))
		d = float(input('d = '))
		c = (a*d)/b
		print(f'{term} is equal to {c}\n')
		
	if term == 'D':
		a = float(input('a = '))
		b = float(input('b = '))
		c = float(input('c = '))
		d = (b*c)/a
		print(f'{term} is equal to {d}\n')	

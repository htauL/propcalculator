exit = False
print('This is the personal proportion calculator from htauL \n\n a/b = c/d\n')


def discover():
    terms = {'A': lambda b, c, d: (b * c) / d,
             'B': lambda a, c, d: (a * d) / c,
             'C': lambda a, b, d: (a * d) / b,
             'D': lambda a, b, c: (b * c) / a}

    term = input('Which term you want to find?\n\n[a]   [c]\n--- = ---\n[b]   [d]\n\nChoose one: ').upper().strip()

    if term in terms:
        values = [float(input(f'{var} = ')) for var in 'abcd']
        result = terms[term](*values)
        print(f'{term} is equal to {result}\n')
    else:
        print("Invalid Option, Please, select between A, B, C or D.")


def compare():
	print('Please insert the terms of the proportion:\n\n[a]   [c]\n--- = ---\n[b]   [d]\n\n')
	a = float(input('a = '))
	b = float(input('b = '))
	c = float(input('c = '))
	d = float(input('d = '))
	
	result = (a/b)/(c/d)
	
	if result == 1:
		print('Proportions are equal\n\n')
	else:
		print('Proportions are not equal\n\n')

	
	
while exit == False:
	mode = input('Which mode do you want to use?\n\n[1] Discover one term\n[2] Compare proportions\n\nChoose one: ')
	if mode == '1':
		discover()
	if mode == '2':
		compare()
	

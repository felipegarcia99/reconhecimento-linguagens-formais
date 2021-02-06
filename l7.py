# A = (a, b, c)
# L7 = w|w possui nº ímpar de a
desc = 'w|w possui nº ímpar de a'

import funcutils

Ateste = ['a', 'b', 'c']
wteste = 'babaaabbabab'

def main(w, A):
	count = 0
	try:
		funcutils.analizAlfb(w, A)
		
		for i in range(len(w)):
			if w[i] == 'a':
				count += 1

		if count%2 != 0:
			return [True, 0]
		else:
			raise Exception('w inválida: palavra não possui nº ímpar de a')
	except Exception as e:
		return [False, e]
	
	
if __name__=='__main__':
	main(wteste, Ateste)

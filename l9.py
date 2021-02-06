# A = (a, b, c)
# L9 = w|w possui nº par de a e ímpar de b, ou possui ímpar de a e par de b
desc = 'w|w possui nº par de a e ímpar de b, ou possui ímpar de a e par de b'

import funcutils

Ateste = ['a', 'b', 'c']
wteste = 'babaaabbabab'

def main(w, A):
	counta = 0
	countb = 0
	try:
		funcutils.analizAlfb(w, A)
		
		for i in range(len(w)):
			if w[i] == 'a':
				counta += 1
			if w[i] == 'b':
				countb += 1

		if ((counta%2 == 0) and (countb%2 != 0)) or ((counta%2 != 0) and (countb%2 == 0)):
			return [True, 0]
		else:
			raise Exception('w inválida: palavra não atende aos requisitos')
	except Exception as e:
		return [False, e]
	
	
if __name__=='__main__':
	main(wteste, Ateste)

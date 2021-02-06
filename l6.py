# A = (a, b, c)
# L6 = w|w possui aaa como subpalavra
desc = 'w|w possui aaa como subpalavra'

import funcutils

Ateste = ['a', 'b', 'c']
wteste = 'babaaabbabab'

def main(w, A):
	try:
		funcutils.analizAlfb(w, A)
		
		for i in range(len(w)):
			if w[i] == 'a':
				if (w[i+1] == 'a') and (w[i+2] == 'a'):
					return [True, 0]
		raise Exception('w inválida: palavra não possui aaa')
	except Exception as e:
		return [False, e]
	
	
if __name__=='__main__':
	main(wteste, Ateste)

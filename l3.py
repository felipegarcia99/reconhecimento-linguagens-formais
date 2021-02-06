# A = (0, 1)
# L3 = todas as palavras começam com 1 e terminam com 0
desc = 'todas as palavras começam com 1 e terminam com 0'

import funcutils

Ateste = ['0', '1']
wteste = '100000'

def main(w, A):
	try:
		funcutils.analizAlfb(w, A)
		
		if w[0] == '1' and w[-1] == '0':
			return [True, 0]
		else:
			raise Exception('w inválida: não começa com 1 ou não termina com 0')
	except Exception as e:
		return [False, e]
	
	
if __name__=='__main__':
	main(wteste, Ateste)

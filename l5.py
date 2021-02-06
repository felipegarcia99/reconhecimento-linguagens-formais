# A = (a, b)
# L5 = todas as palavras possuem bab como sufixo
desc = 'todas as palavras possuem bab como sufixo'

import funcutils

Ateste = ['a', 'b']
wteste = 'abababbabab'

def main(w, A):
	try:
		funcutils.analizAlfb(w, A)
		
		if w[len(w)-3:] != 'bab':
			raise Exception('w inválida: palavra não termina com bab')
		else:
			return [True, 0]
	except Exception as e:
		return [False, e]
	
	
if __name__=='__main__':
	main(wteste, Ateste)

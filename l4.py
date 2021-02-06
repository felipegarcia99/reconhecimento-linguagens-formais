# A = (0, 1)
# L4 = todas as palavras contém ao menos três 1
desc = 'todas as palavras contém ao menos três 1'

import funcutils

Ateste = ['0', '1']
wteste = '100011'

def main(w, A):
	count = 0
	try:
		funcutils.analizAlfb(w, A)
		
		for i in range(len(w)):
			if w[i] == '1':
				count += 1
		if count >= 3:
			return [True, 0]
		elif count < 3:
			raise Exception('w inválida: não contém ao menos três 1')
	except Exception as e:
		return [False, e]
	
	
if __name__=='__main__':
	main(wteste, Ateste)

import funcutils

code = '''
import l{a}

result = l{a}.main(w, A)
'''

strdesc = '''
import l{a}

desc = l{a}.desc
'''

# A = ['0', '1']
# A = ['a', 'b', 'c']
A = []
strdict = {}


def main():
	path = funcutils.selectpath()

	while True:
		num = funcutils.lista_arq_lx(path)

		print('Escolha a linguagem:')
		for i in range(1, num + 1):
			print('- L{}: {}'.format(i, funcutils.getdescricoes(strdict, strdesc, i)))
		lang = int(input())

		A = funcutils.selectlang(lang)

		w = input('\nEscreva a palavra: ')

		dict = {'A': A, 'w': w}
		exec(code.format(a=lang), dict)

		result = dict['result']

		print('\nResultado:')
		if result[0]:
			print('Aceita')
		else:
			print('Rejeitada')
			print('Motivo: {}'.format(result[1]))

		input('\nPressione qualquer tecla para continuar...')
		print('\n')


if __name__ == '__main__':
	main()

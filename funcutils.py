import os

def analizAlfb(w, A):
	for i in range(len(w)):
		if w[i] not in A:
			raise Exception('w inválida: caracteres inválidos')


def getdescricoes(dict, str, i):
	exec(str.format(a=i), dict)
	desc = dict['desc']
	return desc


def selectlang(opc):
	if 1 <= opc <= 4:
		A = ['0', '1']
	elif opc == 5:
		A = ['a', 'b']
	elif 6 <= opc <= 9:
		A = ['a', 'b', 'c']
	return A


def selectpath():
	arq = open(resource_path('arquivos\\caminho.txt'), 'r')
	path = arq.readline()
	return path


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2",os.path.abspath("."))

    return os.path.join(base_path, relative_path)


def lista_arq_lx(path):
	countpy = 0
	listarq = []
	listtemp = os.listdir(path)	
	for i in listtemp:
		if i[len(i)-3:] == '.py':
			listarq.append(i)
	# print(listarq)

	for i in listarq:
		# print(i)
		try:
			if ((i[0] == 'l') and (type(int(i[1])) == int)):
				countpy += 1
		except:
			pass

	# print(countpy)
	return countpy

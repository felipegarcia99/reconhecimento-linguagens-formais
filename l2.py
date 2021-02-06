# A = (0, 1)
# L2 = todas as palavras contém ao menos um 1
desc = 'todas as palavras contém ao menos um 1'

import funcutils

Ateste = ['0', '1']
wteste = '100000'


def main(w, A):
    count = 0
    try:
        funcutils.analizAlfb(w, A)

        for i in range(len(w)):
            if w[i] == '1':
                count += 1
        if count == 0:
            raise Exception('w inválida: não houve 1')
        else:
            return [True, 0]
    except Exception as e:
        return [False, e]


if __name__ == '__main__':
    main(wteste, Ateste)

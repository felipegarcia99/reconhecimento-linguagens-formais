# A = (0, 1)
# L1 = todas as palavras começam com 1
desc = 'todas as palavras começam com 1'

import funcutils

Ateste = ['0', '1']
wteste = '10210101'


def main(w, A):
    try:
        funcutils.analizAlfb(w, A)

        if w[0] != '1':
            raise Exception('w inválida: não começa com 1')
        return [True, 0]
    except Exception as e:
        return [False, e]


if __name__ == '__main__':
    main(wteste, Ateste)

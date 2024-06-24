def jogo(numb):
    if (numb % 3 == 0) & (numb % 5 == 0):
        return 'romeu e julieta'
    if numb % 3 == 0:
        return 'queijo'
    if numb % 5 == 0:
        return 'goiabada'
    return numb
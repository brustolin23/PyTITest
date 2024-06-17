from codigo.game import jogo

def test_quando_jogo_receber_1_entao_retorna_1():
    entrada = 1
    esperado = 1
    resultado = jogo(entrada)
    assert resultado == esperado

def test_quando_jogo_receber_2_entao_retorna_2():
    entrada = 2
    esperado = 2
    resultado = jogo(entrada)
    assert resultado == esperado
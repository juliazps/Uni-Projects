import pytest
import atividade_estrategia_gulosa as atv


@pytest.mark.parametrize('inicio,fim,resp',
[([],[],[]),
([1,5,10], [3,7,12], [0,1,2]),
([1,5,10], [6,7,12], [0,2]),
([1,3,0,5,6,5], [2,4,6,7,9,9], [0,1,3]),
([13,14,15,16,17,18], [15,15,17,18,18,20], [0,2,4,5]),
([6,0,3,5,6,8,10,12], [12,13,14,14,14,15,15,16], [0,7])])
def test_seleciona_aulas(inicio, fim, resp):
	try:
		resultado = atv.seleciona_aulas(inicio, fim)
	except:
		raise AssertionError('Erro ao executar a função seleciona_aulas()')
	if len(resp) == 0:
		assert resultado == resp, 'A função deve retornar uma lista vazia se as listas de horários forem vazias'
	else:
		assert resultado == resp, 'Se horarios_inicio = {0} e horarios_fim = {1}, a função deve retornar {2}'.format(inicio, fim, resp)
	

@pytest.mark.parametrize('carteira,troco,resp',
[([5],5,[5]),
([1,5,10], 6, [1,5]),
([1,1,1,5], 7, [1,1,5]),
([1,1,1,2,2,2,10,25], 17, [1,1,1,2,2,10]),
([1,1,1,1,1,1,2,2,5,5,10,25], 25, [1,1,1,1,1,1,2,2,5,10]),
([1,2,5,5,5,5,10,10,10,25,25,50,50], 47, [2,5,5,5,10,10,10])])
def test_troco_menores_moedas(carteira, troco, resp):
	try:
		resultado = atv.troco_menores_moedas(carteira, troco)
	except:
		raise AssertionError('Erro ao executar a função troco_menores_moedas()')
	assert resultado == resp, 'Se carteira = {0} e valor_troco = {1}, a função deve retornar {2}'.format(carteira, troco, resp)

if __name__ == '__main__':
	pytest.main()

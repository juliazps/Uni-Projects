import pytest
import os.path
import re
import atividade_ordenacao


class ListaEspecial(list):

	def __init__(self, *args):
		super().__init__(*args)
		self.__counter = {}

	def __getitem__(self, key):
		if key < 0:
			key = self.__len__() + key
		if key not in self.__counter:
			self.__counter[key] = 0
		self.__counter[key] += 1
		return super().__getitem__(key)
	
	def sort(self):
		raise AssertionError("Proibido utilizar o método sort()")

	def get_counters(self):
		return self.__counter


def possui_comando_proibido(arqNome):
	if os.path.exists(arqNome):
		with open(arqNome, 'r') as arq:
			txt = arq.read()
			txt = re.sub(r'(?is)([\"]{3}\s*(.*?)\s*[\"]{3})|([\']{3}\s*(.*?)\s*[\']{3})', '', txt)
			if re.search(r'(list\s*[(])|(list(\s|,))|(sort\s*[(])|(sorted(\s|,|\s*[(]))|(map(\s|,|\s*[(]))|(test_ordenacao)', txt):
				return True
	return False


def checa_contadores(lista, min, max):
	assert isinstance(lista, ListaEspecial), 'A lista não deve ter o seu tipo alterado'
	x = lista.get_counters()
	for k, contagem in lista.get_counters().items():
		assert contagem >= min and contagem <= max, 'Seu algoritmo não resolve o problema de maneira eficiente.'


def compara_acessos_lista(dict_contadores, dict_esperado, tol_individual, tol_soma_total):
	qtdAcessosTotal = sum(dict_contadores.values())
	qtdAcessosEsperado = sum(dict_esperado.values())
	if qtdAcessosTotal == 0 or (qtdAcessosTotal < (qtdAcessosEsperado-tol_soma_total)) or (qtdAcessosTotal > (qtdAcessosEsperado+tol_soma_total)):
		return False
	for k, v in dict_contadores.items():
		if not ((v == dict_esperado[k]) or (v == dict_esperado[k]-tol_individual) or (v == dict_esperado[k]+tol_individual)):
			return False
	return True


@pytest.mark.parametrize('lista', [ListaEspecial([2,1]), ListaEspecial([1,3,2]), ListaEspecial([4, 1, 2, 3]),
ListaEspecial([10,20,30,40,10]),ListaEspecial(['pedro', 'maria', 'jose', 'joao', 'ana'])])
def test_lista_nao_ordenada(lista):
	assert not possui_comando_proibido('atividade_ordenacao.py'), 'O código utiliza comandos proibidos'
	try:
		resultado = atividade_ordenacao.esta_ordenada(lista)
	except:
		raise AssertionError('Erro ao executar o código')
	else:
		assert resultado == False, 'A função esta_ordenada() deveria devolver (retornar) False'
		checa_contadores(lista, 1, 2)


@pytest.mark.parametrize('lista', [ListaEspecial([1,12]), ListaEspecial([1,2,11]), ListaEspecial([2,4,4,8]),
ListaEspecial(['ana', 'joao', 'jose', 'maria', 'pedro']),ListaEspecial([2,2,88,300,301,302,999,1021,2048,504123])])
def test_lista_ordenada(lista):
	assert not possui_comando_proibido('atividade_ordenacao.py'), 'O código utiliza comandos proibidos'
	try:
		resultado = atividade_ordenacao.esta_ordenada(lista)
	except:
		raise AssertionError('Erro ao executar o código')
	else:
		assert resultado == True, 'A função esta_ordenada() deveria devolver (retornar) True'
		checa_contadores(lista, 1, 2)


@pytest.mark.parametrize('lista', [ListaEspecial([1]), ListaEspecial([500])])
def test_lista_ordenada_pequena(lista):
	assert not possui_comando_proibido('atividade_ordenacao.py'), 'O código utiliza comandos proibidos'
	try:
		resultado = atividade_ordenacao.esta_ordenada(lista)
	except:
		raise AssertionError('Erro ao executar o código')
	else:
		assert resultado == True, 'A função esta_ordenada() deveria devolver (retornar) True'
		checa_contadores(lista, 1, 2)


@pytest.mark.parametrize('lista', [ListaEspecial([1]), ListaEspecial([500])])
def test_lista_ordenada_pequena(lista):
	assert not possui_comando_proibido('atividade_ordenacao.py'), 'O código utiliza comandos proibidos'
	try:
		resultado = atividade_ordenacao.esta_ordenada(lista)
	except:
		raise AssertionError('Erro ao executar o código')
	else:
		assert resultado == True, 'A função esta_ordenada() deveria devolver (retornar) True'
		checa_contadores(lista, 1, 2)


@pytest.mark.parametrize('lista,acessos,tol_individual,tol_soma_total,lista_ord', 
	[([2,1], {0: 2, 1: 2}, 1, 4, [1,2]),
	([1,2,3,4], {0: 1, 1: 2, 2: 2, 3: 1}, 1, 4, [1,2,3,4]),
	([50,10,20,30,40], {0: 3, 1: 6, 2: 6, 3: 5, 4: 2}, 1, 5, [10,20,30,40,50]),
	(['ana','carlos','bia','diego','eduardo','maria'], {0: 2, 1: 5, 2: 5, 3: 4, 4: 3, 5: 1}, 1, 6, ['ana','bia','carlos','diego','eduardo','maria']),
	([18,5,10,88,40,50,60], {0: 3, 1: 6, 2: 5, 3: 5, 4: 6, 5: 5, 6: 2}, 1, 7, [5,10,18,40,50,60,88]),
	([20,10,30,50,60,40,70,90,80], {0: 4, 1: 7, 2: 6, 3: 7, 4: 8, 5: 7, 6: 5, 7: 4, 8: 2}, 1, 9, [10,20,30,40,50,60,70,80,90]),
	([11,22,33,44,55,66,77,99,88], {0: 2, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 2}, 1, 9, [11,22,33,44,55,66,77,88,99]),
	([11,33,22,44,66,55,77,99,88,100,122,111,133,155,144], {0: 2, 1: 5, 2: 5, 3: 4, 4: 5, 5: 5, 6: 4, 7: 5, 8: 5, 9: 4, 10: 5, 11: 5, 12: 4, 13: 4, 14: 2}, 1, 15, [11,22,33,44,55,66,77,88,99,100,111,122,133,144,155]) ])
def test_lista_ordenacao_bolha(lista, acessos, tol_individual, tol_soma_total, lista_ord):
	assert not possui_comando_proibido('atividade_ordenacao.py'), 'O código utiliza comandos proibidos'
	try:
		resultado = ListaEspecial(lista)
		atividade_ordenacao.ordenacao_bolha(resultado)
	except:
		raise AssertionError('Erro ao executar o código')
	else:
		assert list(resultado) == lista_ord, 'A função ordenacao_bolha() não está ordenando a lista'
		assert compara_acessos_lista(resultado.get_counters(), acessos, tol_individual, tol_soma_total), 'A função ordenacao_bolha() não ordena a lista de maneira eficiente, conforme o enunciado'


if __name__ == '__main__':
	pytest.main()


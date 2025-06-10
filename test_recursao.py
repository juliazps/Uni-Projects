from bdb import Bdb
import sys
import os.path
import pytest

import atividade_recursao as atv

class RecursionDetected(Exception):
	pass

class RecursionDetector(Bdb):
	def do_clear(self, arg):
		pass

	def __init__(self, *args):
		Bdb.__init__(self, *args)
		self.stack = set()

	def user_call(self, frame, argument_list):
		code = frame.f_code
		if code in self.stack:
			raise RecursionDetected
		self.stack.add(code)

	def user_return(self, frame, return_value):
		self.stack.remove(frame.f_code)


def has_iteration(arqNome):
	if os.path.exists(arqNome):
		with open(arqNome, 'r') as arq:
			txt = arq.read()
			if 'while' in txt or 'for ' in txt:
				return True
	return False


def use_recursion(func):
	detector = RecursionDetector()
	detector.set_trace()
	try:
		func()
	except RecursionDetected:
		return True
	else:
		return False
	finally:
		sys.settrace(None)


@pytest.mark.parametrize('n,resultado', [(2,3), (10,55), (14,105), (16,136), (27,378)])
def test_somatorio(n, resultado):
	try:
		assert not has_iteration('atividade_recursao.py') and use_recursion(lambda: atv.somatorio(n))
	except:
		raise AssertionError('Função somatorio não utiliza recursão corretamente')
	try:
		assert resultado == atv.somatorio(n)
	except:
		raise AssertionError('Erro no resultado da função somatorio')


@pytest.mark.parametrize('n,resultado', [(4,True), (6,False), (10,False), (64,True), (512,True)])
def test_potencia_de_2(n, resultado):
	try:
		assert not has_iteration('atividade_recursao.py') and use_recursion(lambda: atv.potencia_de_2(n))
	except:
		raise AssertionError('Função potencia_de_2 não utiliza recursão corretamente')
	try:
		assert resultado == atv.potencia_de_2(n)
	except:
		raise AssertionError('Erro no resultado da função potencia_de_2')


@pytest.mark.parametrize('n,resultado', [(4,1), (10,2), (100,3), (999,3), (267984652,9)])
def test_qtd_digitos(n, resultado):
	try:
		assert not has_iteration('atividade_recursao.py') and use_recursion(lambda: atv.qtd_digitos(n))
	except:
		raise AssertionError('Função qtd_digitos não utiliza recursão corretamente')
	try:
		assert resultado == atv.qtd_digitos(n)
	except:
		raise AssertionError('Erro no resultado da função qtd_digitos')


@pytest.mark.parametrize('n,resultado', [(9,9), (83,11), (471,12), (12345,15), (267984652,49)])
def test_soma_digitos(n, resultado):
	try:
		assert not has_iteration('atividade_recursao.py') and use_recursion(lambda: atv.soma_digitos(n))
	except:
		raise AssertionError('Função soma_digitos não utiliza recursão corretamente')
	try:
		assert resultado == atv.soma_digitos(n)
	except:
		raise AssertionError('Erro no resultado da função soma_digitos')


@pytest.mark.parametrize('n,i,resultado', [([1,2,3],0,6), ([1,2,3],1,5), ([3, 5, 20, 55, 71],2,146),
([11,22,33,44,55,66],0,231), ([11,22,33,44,55,66],5,66)])
def test_soma_lista(n, i, resultado):
	try:
		assert not has_iteration('atividade_recursao.py') and use_recursion(lambda: atv.soma_lista(n, i))
	except:
		raise AssertionError('Função soma_lista não utiliza recursão corretamente')
	try:
		assert resultado == atv.soma_lista(n, i)
	except:
		raise AssertionError('Erro no resultado da função soma_lista')


if __name__ == '__main__':
	pytest.main()


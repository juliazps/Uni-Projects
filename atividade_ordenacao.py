# Análise e Projeto de Algoritmos
# AC2: Ciência da Computação
#
# Email Impacta: julia.peres@aluno.faculdadeimpacta.com.br


"""
ATENÇÃO: nesta AC estão proibidos comandos como: sort(), sorted(), list(), e similares.
Você deve construir as funções solicitadas sem fazer uso de funções auxiliares do Python.
Também não reaproveite as funções da atividade.

Funções permitidas: len() e range().

Não obedecer essas regras pode resultar na anulação da sua atividade!
"""


def esta_ordenada(lista):
	n = len(lista)
	for i in range(n-1):
		if lista[i] > lista[i+1]:
			return False
	return True
	pass


def ordenacao_bolha(lista):
	n = len(lista)
	trocou = True
    
	while trocou:
		trocou = False
		for i in range(1, n):
			if lista[i-1] > lista[i]:
				lista[i-1], lista[i] = lista[i], lista[i-1]
				trocou=True
		n-=1 
	pass
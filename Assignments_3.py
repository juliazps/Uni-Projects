# Análise e Projeto de Algoritmos
# AC3: Ciência da Computação


def seleciona_aulas(horarios_de_inicio, horarios_de_fim):
	aulas_possiveis = []
	fim_anterior = 0 #horario que acabou a aula anterior

	for i, horarios_de_inicio in enumerate(horarios_de_inicio):
		if fim_anterior <= horarios_de_inicio:
			aulas_possiveis.append(i)
			fim_anterior = horarios_de_fim[i]

	return aulas_possiveis



def troco_menores_moedas(carteira, valor_troco):
	moedas_escolhidas = []
	soma = 0

	for i in carteira:
		if soma < valor_troco:
			soma += i
			moedas_escolhidas.append(i)

	for i in range(len(moedas_escolhidas)-1,-1,-1):
		novo = soma - moedas_escolhidas[i]
		if novo >= valor_troco:
			soma -= moedas_escolhidas[i]
			moedas_escolhidas.pop(i)				
			
	return moedas_escolhidas
troco_menores_moedas([1,1,1,5], 7)

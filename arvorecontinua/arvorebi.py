arvore = []
altura = 0
recente = 0
choose = 0

def haltura(ref):
	pai = int((ref-1)/2)
	cont = 2
	while pai > 0: 
		pai = int((pai-1)/2)
		cont+=1
	return cont

def alocar(ref):
	global altura
	aux = haltura(ref)
	if aux > altura :
		altura+=1
		for i in range(0, pow(2, altura)):
			arvore.append(0)

def addfilho(ref):
	posicao = 0
	if not arvore[2*ref+1]:
		posicao = 2*ref+1
	elif not arvore[2*ref+2]:
		posicao = 2*ref+2
	else:
		print("Os filhos desse pai já estão preenchidos")
		return
	arvore[posicao] = input("Digite o valor chave: ")
	global recente
	recente = posicao

def remover(ref):
	global altura
	aux = haltura(ref)
	aux = altura+1-aux
	arvore[ref] = 0	
	if aux>0:
		for i in range(1, 3):
			return remover(2*ref+i)


def buscavertical(chave, ref, alt):
	if str(arvore[ref]) == str(chave):
		return ref
	elif alt+1 <= altura:
		for i in range(1, 3):
			temp=buscavertical(chave, 2*ref+i, alt+1)
			if temp>=0:
				return temp
	return -1

def buscahorizontal(chave, ref, alt):
	cont = 0
	aux = 0
	while cont<=pow(2, alt):
		for i in range(0, 2):
			if (ref+i+aux)>=len(arvore):
				return -1
			if str(arvore[ref+i+aux]) == str(chave):
				return ref+i+aux
			cont+=1
		aux = cont*pow(2, alt-1)
	if alt+1 <= altura:
		for i in range(1, 3):
			temp=buscahorizontal(chave, 2*ref+i, alt+1)
			if temp>=0:
				return temp					
	return -1

#MAIN

arvore.append(input("Defina a raiz: "))
while choose!='6':
	print()
	print()
	print("_____MENU_____")
	print()
	print(" 1 - Adicionar filho")
	print(" 2 - Adicionar irmão")
	print(" 3 - Buscar elemento")
	print(" 4 - Remover elemento")
	print(" 5 - Vetor")
	print(" 6 - Sair")
	print()
	print("______________")
	print()
	choose = input() 
	print()

	if choose=='1':
		print("Onde adicionar?")
		print()
		print(" 1 - Especificar pai")
		escolha = input(" 2 - Elemento mais recente(último adicionado)\n")

		if escolha == '2':
			alocar(recente)
			addfilho(recente)

		if escolha == '1':
			temp = input("Digite a chave do pai referencia: ")
			temp = buscavertical(temp, 0, 0)
			if temp>=0:
				alocar(temp)
				addfilho(temp)
			else:
				print("O elemento NÂO está presente na árvore")
	
	if choose=='2':
		temp = int((buscavertical(input("Digite a chave do irmão referencia: "), 0, 0)-1)/2)
		if temp!=None:
			addfilho(temp)
		

	if choose=='3':
		print()
		chave = input("Digite a chave a ser buscada: ")
		temp = buscahorizontal(chave, 0, 0)
		if temp>=0:
			print("O elemento está na posicao: ", temp)
		else:
			print()
			print("O elemento NÂO está presente na árvore")

	if choose=='4':
		print()
		temp=input("Digite a chave a ser deletada: ")
		temp=buscavertical(temp, 0, 0)
		remover(temp)

	if choose=='5':
		for i in range(0, len(arvore)):
			print(arvore[i], end=' ')

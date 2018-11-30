class node:
	def __init__(self, chave):
		self.pai = None
		self.filhos = [0]
		self.chave = chave

class Trie:
	def __init__(self):
		self.raiz = node(None)
	
	def busca(self, no, chave, cont):
		for i in range(1, len(no.filhos)):
			if chave[:1]==no.filhos[i].chave:
				return self.busca(no.filhos[i], chave[1:], cont+1)
		return [no, cont]
	
	def inserir(self, no, chave, cont):
		if len(chave)==0:
			no.filhos[0]-=1
			return
		if no==self.raiz:
			temp = self.busca(self.raiz, chave, 0)
			no = temp[0]
			cont = temp[1]
			if cont==len(chave):
				no.filhos[0]-=1
				return
			chave = chave[cont:]
		else:
			temp = self.busca(no, chave, 0)
			no = temp[0]
		aux = node(str(chave[:1]))
		aux.pai = no
		no.filhos.append(aux)
		ult=no.filhos[-1]
		aux = len(no.filhos)-1
		while aux>1 and no.filhos[aux-1].chave>ult.chave:
			no.filhos[aux] = no.filhos[aux-1]
			aux-=1 
		no.filhos[aux] = ult
		return self.inserir(no.filhos[aux], chave[1:], cont+1)

	def printar(self, no, print_counter):
		for i in range(1, print_counter):
			if print_counter-5>0 and print_counter-5==i:
				print('└', end='')
			if print_counter-5<=i:
				print("—", end='')
			else:
				print(' ', end='')
		if no!=self.raiz:
			print(no.chave)		
		for i in range(1, len(no.filhos)):
			self.printar(no.filhos[i], print_counter+5)

	def remover(self, chave):
		aux = self.busca(self.raiz, chave, 0)[0]
		while aux.pai:
			temp = aux.pai
			if len(aux.filhos)<=1:
				temp.filhos.remove(aux)
			else:
				return
			aux = temp

	def ler(self, no, palavra, lista):
		if no!=self.raiz:
			palavra += no.chave
			if no.filhos[0]<0:
				for i in range(no.filhos[0]*-1):
					lista.append(palavra)
		for i in range(1, len(no.filhos)):
			self.ler(no.filhos[i],palavra, lista)
		return lista

#MAIN
choose=0
a = Trie()
while choose!='6':
	print()
	print()
	print("_____MENU_____")
	print()
	print(" 1 - Visualizar árvore")
	print(" 2 - Adicionar chave")
	print(" 3 - Remover chave")
	print(" 4 - Listar chaves")
	print(" 5 - Buscar chave")
	print(" 6 - Sair")
	print()
	print("______________")
	print()
	choose = input() 
	print()

	if choose=='1':
		a.printar(a.raiz, 0)
	if choose=='2':
		a.inserir(a.raiz, input("Digite a chave a ser adicionada: "), 0)
	if choose=='3':
		a.remover(input("Digite a chave a ser removida: "))
	if choose=='4':
		print(', '.join(a.ler(a.raiz, '', [])))
	if choose=='5':
		chave = input("Digite a chave a ser encontrada: ")
		temp = a.busca(a.raiz, chave, 0)[0]
		print()
		if temp.filhos[0]!=0 and temp.chave==chave[-1:]:
			print("A chave existe!")
		else:
			print("A chave NÃO existe!")
	if choose=='7':
		print("*")
		print("*")
		print("*")
		print("———————Demonstração———————")
		nomes = ["Raquel Cortês", "Marcelo Clementino", "Tadeu Fragoso", "Sabrina Gois", "Tadeu Ferreira"]
		print("\n\n\n\n")
		print("Lista de Nomes:\n", nomes)
		print("\n\n\n\n")
		input()
		print("**Adicionando", nomes[0], "**")
		a.inserir(a.raiz, nomes[0], 0)
		print("\n\n\n\n")
		input()
		print("          Árvore")
		a.printar(a.raiz, 0)
		print("\n\n\n\n")
		input()
		print("**Adicionando ", nomes[2], "**")
		print("\n\n\n\n")
		a.inserir(a.raiz, nomes[2], 0)
		input()
		print("          Árvore")
		a.printar(a.raiz, 0)
		input()
		print("\n\n\n\n")
		print("**Lendo nomes**")
		print("\nNomes Lidos:\n")
		print(', '.join(a.ler(a.raiz, '', [])))
		print("\n\n\n\n")
		input()
		print("**Adicionando semelhante ", nomes[4], "**")
		print("\n\n\n\n")
		input()
		a.inserir(a.raiz, nomes[4], 0)
		print("          Árvore")
		a.printar(a.raiz, 0)
		input()
		print()
		print("\n\n\n\n")
		print("**Deletando nome Tadeu Fragoso**")
		print("\n\n\n\n")
		input()
		a.remover(nomes[2])
		print("          Árvore")
		a.printar(a.raiz, 0)
		input()
		print("\n\n\n\n")
		print("**Adicionando mesmo nome Raquel Cortês**")
		input()
		a.inserir(a.raiz, nomes[0], 0)
		print("          Árvore")
		a.printar(a.raiz, 0)
		print("\n\n\n\n")
		input()
		print("**Lendo nomes**")
		print("\nNomes Lidos:\n")
		print(', '.join(a.ler(a.raiz, '', [])))
		print("\n\n\n\n")
		input()
		print("**Buscando nome Tadeu Ferreira**")
		print("\n\n\n\n")
		temp = a.busca(a.raiz, nomes[4], 0)[0]
		print()
		if temp.filhos[0]!=0 and temp.chave==nomes[4][-1:]:
			print("A chave existe!")
		else:
			print("A chave NÃO existe!")
		print("\n\n\n\n")
		input()
		print("**FIM**")
		input()
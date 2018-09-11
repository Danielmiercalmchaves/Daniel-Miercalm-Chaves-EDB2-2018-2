#include <iostream>
using std::cout;
using std::cin;
using std::endl;

int hash(int dado, int n, int tentativa) {
	return (dado+tentativa)%n;
}

void inserir(int *vetor, int n, int dado) {
	int tentativa=0;
	while(vetor[hash(dado, n, tentativa)]) {
		tentativa++;
		if(tentativa>n)return;
	}
	vetor[hash(dado, n, tentativa)] = dado;
}

int acessar(int *vetor, int n, int dado) {
	int tentativa=0;
	while(vetor[hash(dado, n, tentativa)]!=dado) {
		if(vetor[hash(dado, n, tentativa)]) return -1;
		tentativa++;
		if(tentativa>n)return -1;
	}
	return hash(dado, n, tentativa);
}

void remover(int *vetor, int n, int dado) {
	int aux = acessar(vetor, n, dado);
	if(aux!=-1)vetor[aux] = 0;
}

int main() {
	int tamanho, *v, ch=0, temp;
	cout << "Digite o tamanho do vetor: ";
	cin >> tamanho;
	v = new int[tamanho]();
	while(ch!=5) {
		cout << endl << endl << "Escolha a operação: " << endl;
		cout << endl << "1 - Inserir" << endl << "2 - Remover" << endl << "3 - Buscar" << endl << "4 - Visualizar Vetor" << endl << "5 - Sair" << endl << endl;
		cin >> ch;
		if(ch==1) {
			cout << endl << "Digite o dado: ";
			cin >> temp;
			inserir(v, tamanho, temp);
		}
		if(ch==2) {
			cout << endl << "Digite o dado: ";
			cin >> temp;
			remover(v, tamanho, temp);			
		}
		if(ch==3) {
			cout << endl << "Digite o dado: ";
			cin >> temp;
			cout << endl << "O dado está na posição " << v[acessar(v, tamanho, temp)] << " do vetor" << endl;
		}
		if(ch==4) {
			cout << endl << "Vetor: " << endl;
			for(int i=0; i<tamanho; i++) cout << v[i] << " ";
			cout << endl;
		}
	}
	return 0;
}
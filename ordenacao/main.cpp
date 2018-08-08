#include <iostream>
#include "ordenadores.hpp"
using namespace std;

int main() {
	int *v, n, ch;
	cout << "Digite o tamanho do vetor: " << endl;
	cin >> n;
	v = new int[n];
	cout << endl << "Digite o vetor(int): " << endl;
	for(int i=0; i<n; i++) cin >> v[i];
	ordenadores a(v, n);
	cout << "Escolha o método de ordenação: " << endl << "1 - Inserction Sort" << endl << "2 - Selection Sort" << endl << endl;
	cin >> ch;
	while(true) {
		if(ch==1) { 
			a.inserction();
			break;
		}
		if(ch==2) {
			a.selection();
			break;
		}
	}
	cout << endl << "Vetor final:" << endl;
	for(int i=0; i<n; i++) cout << v[i] << " ";
	cout << endl;
	return 0;
}
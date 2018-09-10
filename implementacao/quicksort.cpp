#include <iostream>
using namespace std;

void troca(float *v, int i, int j){
	int aux=v[i];
	v[i]=v[j];
	v[j]=aux;
}

int separar(float *v, int n) { 
	int p=0, f1=1, f2=n-1; 
	while(f2>=f1) {
		while(v[f1]<v[p]) f1++; 
		while(v[f2]>v[p]) f2--; 
		if(f1<f2) { 
			troca(v, f1, f2); 
			f1++; f2--;
		} 
	}
	troca(v, f2, p); 
	return f2;
}

void sort(float *v, int n) {
	if(n<=1) return; 
	int p=separar(v, n);
	sort(v, p); 
	sort(v+p+1, n-p-1); 
}

int main() {
	int tamanho;
	cout << "Digite o tamanho do vetor: ";
	cin >> tamanho;
	cout << "Digite o vetor: ";
	float *v = new float[tamanho];
	for(int i=0; i<tamanho; i++)cin >> v[i];
	sort(v, tamanho);
	cout << "Vetor final: " << endl;
	for(int i=0; i<tamanho; i++)cout << v[i] << " ";
	cout << endl;
	return 0;
}
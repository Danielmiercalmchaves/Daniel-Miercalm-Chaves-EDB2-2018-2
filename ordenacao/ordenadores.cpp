#include <iostream>
#include "ordenadores.hpp"

ordenadores::ordenadores(int *v, int n) {
	this->v = v;
	this->n = n;
}

void ordenadores::inserction() {
	for (int i=0; i<n; i++) {
		int ult=v[i];
		int j = i;	
		while(j>0 && v[j-1]>ult){ 
			v[j] = v[j-1]; 
			j--; 
		}
		v[j] = ult; 
	}
}

void ordenadores::selection() {
	for(int i=0; i<n; i++) { 
		int pos = i;
		for(int j=i+1; j<n; j++) {
			if(v[pos]>v[j]) { 
			pos = j; 
		 	}
		}
	int temp = v[i];
	v[i] = v[pos];
	v[pos] = temp;		
	}
}
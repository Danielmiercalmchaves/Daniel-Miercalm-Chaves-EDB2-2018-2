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

void ordenadores::merge() {
	merge1(this->v, this->n);
}

void ordenadores::merge1(int *vt, int s) {
	if(s>1) {
		merge1(vt,s/2); 
		merge1(vt+s/2, s-s/2);
		merge2(vt, s);
	}
}

void ordenadores::merge2(int *vt, int s) {
	int *temp = new int[s];
	int p=0, q=s/2, r=0;
	if(vt[p]<vt[q]){ 
		temp[r] = vt[p];
		r++;
		p++;
	} 
	else {
		temp[r] = vt[q]; 
		r++;
		q++;
	}
	while(p<s/2) { 
		temp[r] = vt[p];
		r++;
		p++;
	}
	while(q<s) { 
		temp[r] = vt[q];
		r++;
		q++;
	}
	for(r=0; r<s; r++) vt[r]=temp[r]; 
	delete temp;
}

void ordenadores::troca(int *vt, int i, int j){
	int aux=vt[i];
	vt[i]=vt[j];
	vt[j]=aux;
}

void ordenadores::quick() {
	quick1(this->v, this->n);
}

int ordenadores::quick2(int *vt, int s) { 
	int p=0, f1=1, f2=s-1;
	while(f2>f1) {
		while(vt[f1]<vt[p]&&f1<f2) f1++; 
		while(vt[f2]>vt[p]) f2--; 
		if(f1<f2) troca(vt, f1, f2);
	}
	troca(vt, f2, p);
	return f2;
}

void ordenadores::quick1(int *vt, int s) {
	if(s<=1) return; 
	int p=quick2(vt, s);
	quick1(vt, p); 
	quick1(vt+p+1, s-p-1); 
}


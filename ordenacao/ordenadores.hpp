#ifndef ORDENADORES_HPP
#define ORDENADORES_HPP

class ordenadores {
	private:
		int *v;
		int n;
	public:
		ordenadores(int *v, int n);
		void inserction();
		void selection();
		void merge();
		void merge1(int *vt, int s);
		void merge2(int *vt, int s);
		void troca(int *vt, int i, int j);
		void quick();
		void quick1(int *vt, int s);
		int quick2(int *vt, int s);
};

#endif
a.out: main.o ordenadores.o
	g++ main.o ordenadores.o -o a.out

main.o:
	g++ -c main.cpp

ordenadores.o: ordenadores.hpp
	g++ -c ordenadores.cpp

clean:
	rm -f *.o
#include <iostream>

#include "endereco.hpp"
#include "contato.hpp"
#include "motorista.hpp"
#include "cliente.hpp"
#include "carga.hpp"
#include "veiculo.hpp"

int main() {

	std::string a = std::string("asdqq");

	Contato* contato = new Contato(a, a, a);
	Endereco* endereco = new Endereco(a, a, a, a, a, a);
	Cliente* c = new Cliente(a, a, contato, endereco, 12);
	Motorista* m = new Motorista(1, a, a, 12, 0, contato, endereco, 1200);
    Carga* carga = new Carga(1, a, 12, a, a, 2, 3, 4, a, c);
    Veiculo* v = new Veiculo(1, "qwe", "ttt", 99, true);
    v->addCarga(carga);
    v->setMotorista(m);


    std::cout << v->getCor() << '\n';


	return 0;
}

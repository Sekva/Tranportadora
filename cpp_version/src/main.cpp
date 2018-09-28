#include <iostream>

#include "endereco.hpp"
#include "contato.hpp"

#include "cliente.hpp"

int main() {

	std::string a = std::string("asdqq");

	Contato* contato = new Contato(a, a, a);
	Endereco* endereco = new Endereco(a, a, a, a, a, a);
	Cliente* c = new Cliente(a, a, contato, endereco, 12);
	std::cout << c->getEndereco()->getRua() << '\n';

	return 0;
}

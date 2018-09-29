#include "cliente.hpp"

Cliente::Cliente(std::string nome, std::string cpf, Contato* contato, Endereco* endereco, int numNotaFiscal) : Pessoa(nome, cpf, contato, endereco) {
	this->modCliente(nome, cpf, contato, endereco, numNotaFiscal);
}

void Cliente::modCliente(std::string nome, std::string cpf, Contato* contato, Endereco* endereco, int numNotaFiscal) {
	this->modPessoa(nome, cpf, contato, endereco);
	this->numNotaFiscal = numNotaFiscal;
}

int Cliente::getNumNotaFiscal() {
	return this->numNotaFiscal;
}

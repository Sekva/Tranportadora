#include "pessoa.hpp"

Pessoa::Pessoa(std::string nome, std::string cpf, Contato* contato, Endereco* endereco) {
	this->modPessoa(nome, cpf, contato, endereco);
}

void Pessoa::modPessoa(std::string nome, std::string cpf, Contato* contato, Endereco* endereco) {
	this->nome = nome;
	this->cpf = cpf;
	this->contato = contato;
	this->endereco = endereco;
}

std::string Pessoa::getNome() {
	return this->nome;
}

std::string Pessoa::getCpf() {
	return this->cpf;
}

Contato* Pessoa::getContato() {
	return this->contato;
}

Endereco* Pessoa::getEndereco() {
	return this->endereco;
}

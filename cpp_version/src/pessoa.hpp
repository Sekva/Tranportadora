#ifndef PESSOA_HPP
#define PESSOA_HPP

#include <string>
#include "contato.hpp"
#include "endereco.hpp"

class Pessoa {

	private:
		std::string nome;
		std::string cpf;
		Contato* contato;
		Endereco* endereco;
	public:
		Pessoa(std::string nome, std::string cpf, Contato* contato, Endereco* endereco);
		void modPessoa(std::string nome, std::string cpf, Contato* contato, Endereco* endereco);
		std::string getNome();
		std::string getCpf();
		Contato* getContato();
		Endereco*getEndereco();

};

#endif

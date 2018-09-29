#ifndef CLIENTE_HPP
#define CLIENTE_HPP

#include "pessoa.hpp"

class Cliente : public Pessoa {

	private:
		int numNotaFiscal;
	public:
		Cliente(std::string nome, std::string cpf, Contato* contato, Endereco* endereco, int numNotaFiscal);
		void modCliente(std::string nome, std::string cpf, Contato* contato, Endereco* endereco, int numNotaFiscal);
		int getNumNotaFiscal();

};


#endif

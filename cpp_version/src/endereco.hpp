#ifndef ENDERECO_HPP
#define ENDERECO_HPP

#include <string>

class Endereco {

	private:
		std::string estado;
		std::string cidade;
		std::string bairro;
		std::string rua;
		std::string numeroCasa;
		std::string complemento;
	public:
		Endereco(std::string estado, std::string cidade, std::string bairro, std::string rua, std::string numeroCasa, std::string complemento);
		void modEndereco(std::string estado, std::string cidade, std::string bairro, std::string rua, std::string numeroCasa, std::string complemento);
		std::string infoParciais();
		std::string infoCompleta();

		std::string getEstado();
		std::string getCidade();
		std::string getBairro();
		std::string getRua();
		std::string getNumeroCasa();
		std::string getComplemento();
};


#endif

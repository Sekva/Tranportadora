#ifndef CONTATO_HPP
#define CONTATO_HPP

#include <string>

class Contato {

	private:
		std::string telefone;
		std::string email;
		std::string site;
	public:
		Contato(std::string telefone, std::string email, std::string site);
		void modContato(std::string telefone, std::string email, std::string site);
		std::string getTelefone();
		std::string getEmail();
		std::string getSite();

};
#endif

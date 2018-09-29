#include "contato.hpp"

Contato::Contato(std::string telefone, std::string email, std::string site) {
	this->modContato(telefone, email, site);
}

void Contato::modContato(std::string telefone, std::string email, std::string site) {
	this->telefone = telefone;
	this->email = email;
	this->site = site;
}

std::string Contato::getTelefone() {
	return this->telefone;
}
std::string Contato::getEmail() {
	return this->email;
}
std::string Contato::getSite() {
	return this->site;
}

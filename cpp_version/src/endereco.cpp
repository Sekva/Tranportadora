#include "endereco.hpp"

Endereco::Endereco(std::string estado, std::string cidade, std::string bairro, std::string rua, std::string numeroCasa, std::string complemento) {

	this->modEndereco(estado, cidade, bairro, rua, numeroCasa, complemento);

}

void Endereco::modEndereco(std::string estado, std::string cidade, std::string bairro, std::string rua, std::string numeroCasa, std::string complemento) {

	this->estado = estado;
	this->cidade = cidade;
	this->bairro = bairro;
	this->rua = rua;
	this->numeroCasa = numeroCasa;
	this->complemento = complemento;

}

std::string Endereco::infoParciais() {
	return std::string("ads\n");
}

std::string Endereco::infoCompleta() {
	return std::string("ads1\n");
}

std::string Endereco::getEstado() {
	return this->estado;
}

std::string Endereco::getCidade() {
	return this->cidade;
}

std::string Endereco::getBairro() {
	return this->bairro;
}

std::string Endereco::getRua() {
	return this->rua;
}

std::string Endereco::getNumeroCasa() {
	return this->numeroCasa;
}

std::string Endereco::getComplemento() {
	return this->complemento;
}

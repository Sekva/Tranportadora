#include "motorista.hpp"

Motorista::Motorista(int idMotorista, std::string nome, std::string cpf, int idade, int anosTrabalho, Contato* contato, Endereco* endereco, float salario) : Pessoa(nome, cpf, contato, endereco) {
   this->idMotorista = idMotorista;
   this->setMotorista(nome, cpf, idade, anosTrabalho, contato, endereco, salario, true);
};

void Motorista::setMotorista(std::string nome, std::string cpf, int idade, int anosTrabalho, Contato* contato, Endereco* endereco, float salario, bool disponibilidade) {
   this->modPessoa(nome, cpf, contato, endereco);
   this->idade = idade;
   this->anosTrabalho = anosTrabalho;
   this->salario = salario;
   this->disponibilidade = disponibilidade;
};

int Motorista::getId() {
   return this->idMotorista;
};

int Motorista::getIdade() {
   return this->idade;
};

int Motorista::getAnosTrabalhando() {
   return this->anosTrabalho;
};

float Motorista::getSalario(){
   return this->salario;
};

bool Motorista::getDisponibilidade() {
   return this->disponibilidade;
};

void Motorista::setDisponibilidade(bool novaDisponibilidade) {
   this->disponibilidade = novaDisponibilidade;
};

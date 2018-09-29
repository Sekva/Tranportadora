#ifndef MOTORISTA_HPP
#define MOTORISTA_HPP

#include "pessoa.hpp"

class Motorista : public Pessoa {

   private:
      //Tem que ver esse negocio do id, como será atribuído o número. É melhor id do que cpf nesse caso por será mais utilizado para identificação na empresa
      int idMotorista;
      int idade;
      int anosTrabalho;
      float salario;
      bool disponibilidade;
   public:
      Motorista(int idMotorista, std::string nome, std::string cpf, int idade, int anosTrabalhando, Contato* contato, Endereco* endereco, float salario);
      int getId();
      int getIdade();
      int getAnosTrabalhando();
      float getSalario();
      bool getDisponibilidade();

      //Para toda vez que for necessário mudar a disponibilidade do motorista, não ser necessário salvar tudo de novo com o método setMotorista()
      void setDisponibilidade(bool novaDisponibilidade);

      void setMotorista(std::string nome, std::string cpf, int idade, int anosTrabalhando, Contato* contato, Endereco* endereco, float salario, bool disponibilidade);
};

#endif

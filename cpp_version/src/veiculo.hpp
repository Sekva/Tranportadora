#ifndef VEICULO_HPP
#define VEICULO_HPP

#include <iostream>
#include <vector>

#include "carga.hpp"
#include "motorista.hpp"

class Veiculo {
    private:
        int idVeiculo;
        std::string placa;
        std::string cor;
        std::vector<Carga*> cargas;
        float capacidade;
        bool disponibilidade;
        Motorista* motorista;

    public:
        Veiculo(int idVeiculo, std::string placa, std::string cor, float capacidade, bool disponibilidade);
        int getIdVeiculo();

        std::string getPlaca();
        void setPlaca(std::string placa);

        std::string getCor();
        void setCor(std::string cor);

        float getCapacidade();

        bool getDisponibilidade();
        void setDisponibilidade(bool disp);

        Motorista* getMotorista() ;
        void setMotorista(Motorista* motorista);

        void removerCarga(Carga* carga);
        void addCarga(Carga* carga);
};

#endif

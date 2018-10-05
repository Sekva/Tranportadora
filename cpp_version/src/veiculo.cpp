#include "veiculo.hpp"

Veiculo::Veiculo(int idVeiculo, std::string placa, std::string cor, float capacidade, bool disponibilidade)
{
    this->idVeiculo = idVeiculo;
    this->placa = placa;
    this->cor = cor;
    this->capacidade = capacidade;
    this->disponibilidade = disponibilidade;
    this->cargas.clear();
    this->motorista = nullptr;
}

int Veiculo::getIdVeiculo()
{
    return this->idVeiculo;
}

std::string Veiculo::getPlaca()
{
    return this->placa;
}

void Veiculo::setPlaca(std::string placa)
{
    this->placa = placa;
}

std::string Veiculo::getCor()
{
    return this->cor;
}

void Veiculo::setCor(std::string cor)
{
    this->cor = cor;
}

float Veiculo::getCapacidade()
{
    return this->capacidade;
}

bool Veiculo::getDisponibilidade()
{
    return this->disponibilidade;
}

void Veiculo::setDisponibilidade(bool disp)
{
    this->disponibilidade = disp;
}

Motorista* Veiculo::getMotorista()
{
    return this->motorista;
}

void Veiculo::setMotorista(Motorista *motorista)
{
    this->motorista = motorista;
}

void Veiculo::removerCarga(Carga *carga)
{

}

void Veiculo::addCarga(Carga *carga)
{

}

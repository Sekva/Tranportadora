#include "carga.hpp"

Carga::Carga(int idCarga, std::string material, float peso, std::string origem, std::string destino, int periculosidade, float tamanhoContainer, float kmEsperada, std::string dataSaida, Cliente *c) {
    this->idCarga = idCarga;
    this->material = material;
    this->peso = peso;
    this->origem = origem;
    this->destino = destino;
    this->periculosidade = periculosidade;
    this->tamanhoContainer = tamanhoContainer;
    this->kmEsperada = kmEsperada;
    this->dataSaida = dataSaida;
    this->cliente = c;

    switch (this->periculosidade) {
        case 1:
            this->taxa = 1;
            break;
        case 2:
            this->taxa = (float) 1.1;
            break;
        case 3:
            this->taxa = (float) 1.18;
            break;
        case 4:
            this->taxa = (float) 1.25;
            break;
        case 5:
            this->taxa = (float) 1.3;
            break;
        case 6:
            this->taxa = (float) 1.4;
            break;
    }

    this->custoTransporte = (1000 + 3*this->kmEsperada) * this->taxa;
}

int Carga::getId() {
    return this->idCarga;
}

std::string Carga::getMaterial() {
    return this->material;
}

float Carga::getPeso() {
    return this->peso;
}

std::string Carga::getOrigem() {
    return this->origem;
}

std::string Carga::getDestino() {
    return this->destino;
}

int Carga::getPericulosidade() {
    return this->periculosidade;
}

float Carga::getTamanhoContainer() {
    return this->tamanhoContainer;
}

float Carga::getKmEsperada() {
    return this->kmEsperada;
}

float Carga::getKmPercorrido() {
    return this->kmPercorrido;
}

std::string Carga::getDataSaida() {
    return this->dataSaida;
}

std::string Carga::getDataEntrega() {
    return this->dataEntrega;
}

Cliente *Carga::getCliente() {
    return this->cliente;
}

float Carga::getTaxa() {
    return this->taxa;
}

float Carga::getCustoTransporte() {
    return this->custoTransporte;
}

void Carga::setKmPercorrido(float kmPercorrido) {
    this->kmPercorrido = kmPercorrido;
    this->custoTransporte = (1000 + 3 * this->kmPercorrido) * this->taxa;
}

void Carga::setDataEntrega(std::string data) {
    this->dataEntrega = data;
}

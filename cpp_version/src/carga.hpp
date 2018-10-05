#ifndef CARGA_HPP
#define CARGA_HPP

#include "cliente.hpp"
#include <iostream>

class Carga {

	private:
		int idCarga;
		std::string material;
		float peso;
		std::string origem;
		std::string destino;
		int periculosidade;
		float tamanhoContainer;
		float kmEsperada;
		float kmPercorrido;
		std::string dataSaida;
		std::string dataEntrega;
		Cliente* cliente;
		float taxa;
		float custoTransporte;

	public:
		Carga(int idCarga, std::string material, float peso, std::string origem, std::string destino, int periculosidade, float tamanhoContainer, float kmEsperada, std::string dataSaida, Cliente* c);

		int getId();
		std::string getMaterial();
		float getPeso();
        std::string getOrigem();
        std::string getDestino();
        int getPericulosidade();
        float getTamanhoContainer();
        float getKmEsperada();
        float getKmPercorrido();
        std::string getDataSaida();
        std::string getDataEntrega();
        Cliente* getCliente();
        float getTaxa();
        float getCustoTransporte();

        void setKmPercorrido(float tamanho);
        void setDataEntrega(std::string data);

};


#endif

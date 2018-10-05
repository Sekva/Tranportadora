#ifndef MOTORISTA_CRUD_HPP
#define MOTORISTA_CRUD_HPP

#include "motorista.hpp"

class MotoristaCRUD {

	public:
		MotoristaCRUD();
		void cadastrarMotorista(Motorista* motorista);
		void removerMotorista(Motorista* motorista);
		void pegarMotorista(int idMotorista);
		void atualizarMotorista(Motorista* motorista);
		
};

#endif

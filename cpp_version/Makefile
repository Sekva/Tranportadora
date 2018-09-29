LIBFLAGS =
CXX = g++

SRC_DIR = ./src/
OBJECTS_DIR = ./objects/
BUILD_DIR = ./build/

SRCS = main.cpp \
endereco.cpp \
contato.cpp \
pessoa.cpp \
cliente.cpp \
motorista.cpp

BIN_NAME = trans

OBJS = $(SRCS:.cpp=.o)

OBJS_FINAL = $(OBJS:%.o=$(OBJECTS_DIR)%.o)

BIN = $(BUILD_DIR)$(BIN_NAME)

all : $(BIN)

$(BIN) : $(OBJS_FINAL)
	$(CXX) $(OBJS_FINAL) -o $(BIN) $(LIBFLAGS)

$(OBJS_FINAL) : $(OBJECTS_DIR)%.o : $(SRC_DIR)%.cpp
	$(CXX) -c $< -o $@

clean :
	echo $(OBJS_FINAL)
	rm  $(BIN) $(OBJS_FINAL)

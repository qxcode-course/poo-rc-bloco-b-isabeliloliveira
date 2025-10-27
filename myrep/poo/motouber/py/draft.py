class Pessoa:
    def __init__(self):
        self.__nome: str =""
        self.__dinheiro: int=0
        
        def get_nome(self):
            return self.__nome
        
        def get_dinheiro(self):
            return self.__dinheiro
        
        def set_nome(self, nome: str):
            self.__nome=nome
            
        def set_dinheiro(self, dinheiro:int):
            self.__dinheiro=dinheiro
            
        def __str__(self):
            return f"{self.__nome}:{self.__money}"
            
class Moto:
    def __init__(self):
        self.__custo: int=0
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None
        
    
    def setDrive(self, pessoa: Pessoa):
        if self.getDrive() != None:
            print("fail: já tem um motorista")
            return
        self.__motorista = pessoa
        
    def setP(self, pessoa: Pessoa|None):
        if pessoa == None:
            self.__passag=None
            return
        self.__motorista = pessoa
    
    def __str__(self):
        return f"Cost: {}, Driver:{}:{}, Passenger: {}, "
    
def main(self):
    moto = Pessoa
    
    while True:
        line = input()
        print("$" + line )
        args= line.split(" ")
        
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(moto)
        
        elif args[0] == "setPass":
            nome = args[1]
            dinheiro = int(args[2])
            moto.setPass(Pessoa(nome, dinheiro))
            
        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = int(args[2])
            moto.setDriver(Pessoa(nome, dinheiro))
            
        elif args[0] == "drive":
            moto.setCusto(int(args[1]))
            
        elif args[0] == "honk":
            moto.buzinar()

main()
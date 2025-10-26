class Pessoa:
    def __init__(self):
        self.__nome: str =""
        self.__dinheiro: int=0
        
        def get_nome(self):
            return self.__nome
        
        def get_dinheiro(self):
            return self.__dinheiro
            
class Moto:
    def __init__(self):
        self.__custo: int=0
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None
        
    def get_Motorista(self):
        return

    def setDrive(self, pessoa: Pessoa):
        if self.getDrive() != None:
            print("fail: já tem um motorista")
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
        
        elif args[0] == "enter":
            nome = args[1]  
            idade = int(args[2])
            moto.inserir(Pessoa(nome, idade))
            
        elif args[0] == "init":
            moto.set_power(int(args[1]))
            
        elif args[0] == "leave":
            
            pessoa = moto.remover()
            if pessoa == None:
                print("fail: empty motorcycle")
            
            else:
                print(f"{pessoa}")
                
        elif args[0] == "buy":
            moto.buyTime(int(args[1]))
            
        elif args[0] == "drive":
            moto.dirigir(int(args[1]))
        
        elif args[0] == "honk":
            moto.buzinar()

main()
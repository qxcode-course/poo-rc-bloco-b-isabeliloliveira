class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome= nome
        self.__dinheiro= dinheiro
        
    def get_nome(self):
        return self.__nome
        
    def get_dinheiro(self):
        return self.__dinheiro
        
    def set_nome(self, nome: str):
        self.__nome=nome
            
    def set_dinheiro(self, dinheiro:int):
        self.__dinheiro=dinheiro
        
        
    def __str__(self):
        return f"{self.__nome}:{self.__dinheiro}"
            
class Moto:
    def __init__(self):
        self.__custo: int=0
        self.__motorista: Pessoa | None = None
        self.__passag: Pessoa | None = None
        
    
    def setDriver(self, pessoa: Pessoa):
        if self.getDrive() != None:
            print("fail: já tem um motorista")
            return
        self.__motorista = pessoa
        
    def setP(self, pessoa: Pessoa|None):
        if pessoa == None:
            self.__passag=None
            return
        if self.__passag is not None:
            print("fail: já tem um passageiro")
            return
        self.__passag = pessoa
        
    def getDrive(self):
        return self.__motorista
            
    def getPass(self) -> Pessoa | None :
        return self.__passag
        
    def getCusto(self):
        return self.__custo
        
        
        
    def leavePass(self):
            if self.getDrive() is None:
                print("fail: não tem motorista")
                return
            if self.getPass() is None:
                print("fail: não tem um passageiro")
                return
            
            passag = self.getPass()
            motorista = self.getDrive()
            custo = self.getCusto()
            
            if passag.get_dinheiro() < custo:
                print("fail: Passenger does not have enough money")
                motorista.set_dinheiro(motorista.get_dinheiro()+custo)
                passag.set_dinheiro(0)
                self.__custo = 0
                self.__passag = None
                print(f"{passag} left")
                
            else:
                passag.get_dinheiro() >= custo
                motorista.set_dinheiro(motorista.get_dinheiro()+custo)
                passag.set_dinheiro(passag.get_dinheiro()-custo)
                self.__custo = 0
                self.__passag = None
                print(f"{passag} left")
        

    def set_custo(self, custo:int):
        self.__custo += custo
    
    def __str__(self):
        passag = self.__passag if self.__passag != None else "None"
        motorista = self.__motorista if self.__motorista != None else "None"
        return f"Cost: {self.__custo}, Driver: {motorista}, Passenger: {passag}"
    
def main():
    moto = Moto()
    
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
            moto.setP(Pessoa(nome, dinheiro))
            
        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = int(args[2])
            moto.setDriver(Pessoa(nome, dinheiro))
            
        elif args[0] == "drive":
            moto.set_custo(int(args[1]))
            
        elif args[0] == "leavePass":
            moto.leavePass()

main()
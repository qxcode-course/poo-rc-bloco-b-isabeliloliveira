class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        return f"{self.nome}:{self.idade}"
    
class Moto:
    def __init__(self):
        self.__pessoa: Pessoa | None = None #pessoa pode ser pessoa ou pode ser nulo
        self.__potencia: int = 1
        self.__tempo: int = 0
    
    def __str__(self):
        pessoa = self.__pessoa if self.__pessoa != None else "empty"
        return f"power:{self.__potencia}, time:{self.__tempo}, person:({pessoa})"
        
        
    def inserir(self, pessoa: Pessoa) -> bool:
        if self.__pessoa != None:
            print("fail: busy motorcycle")
            return True

        self.__pessoa = pessoa
        return False

    def remover(self) -> Pessoa | None:
        aux = self.__pessoa
        self.__pessoa = None
        return aux

    def set_power(self, valor:int):
        self.__potencia = valor
        
    def buyTime(self, time: int):
        self.__tempo += time
        
    def dirigir(self):
        
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
        
        elif args[0] == "enter":
            nome = args[1]  
            idade = args [2]
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
        
main()
# moto = Moto()
# moto.inserir(Pessoa("fulano"))
# print(moto.pessoa)



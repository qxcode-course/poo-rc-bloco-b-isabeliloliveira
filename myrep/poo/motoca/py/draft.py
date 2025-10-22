class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        return f"{self.nome}:{self.idade}"

    def get_idade(self):
        return self.idade
    
class Moto:
    def __init__(self):
        self.__pessoa: Pessoa | None = None #pessoa pode ser pessoa ou pode ser nulo
        self.__potencia: int = 1
        self.__tempo: int = 0
    
    def __str__(self):
        pessoa = self.__pessoa if self.__pessoa != None else "empty"
        return f"power:{self.__potencia}, time:{self.__tempo}, person:({pessoa})"
        
    
    def get_pessoa(self):
        return self.__pessoa
    

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
        
    def dirigir(self, time: int):
        if self.__tempo ==0:
            print("fail: buy time first")
            return
        if self.__pessoa == None:
            print("fail: empty motorcycle")
            return
        if self.get_pessoa().get_idade()>10:
            print("fail: too old to drive")
            return
        if self.__tempo<time:
            print(f"fail: time finished after {self.__tempo} minutes")
            self.__tempo=0
            return 
        self.__tempo-=time
        
    def buzinar(self):
        letra = "e"
        print("P"+(letra*self.__potencia)+"m")
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
# moto = Moto()
# moto.inserir(Pessoa("fulano"))
# print(moto.pessoa)



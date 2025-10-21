class Camisa:
    def __init__(self):
        self.__tamanho: str = ""
        
    
    def get_tamanho(self):
        return self.__tamanho
    
    def set_tamanho(self, tamanho: str):
        if tamanho.upper()!="PP" and tamanho.upper()!="P" and tamanho.upper()!="M" and tamanho.upper()!="G" and tamanho.upper()!="GG" and tamanho.upper()!="EXG":
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return
        self.__tamanho = tamanho
        
def main():
    camisa = Camisa()
    
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(f"size: ({camisa.get_tamanho()})")
            
        elif args[0] == "size":
            camisa.set_tamanho(args[1])
   
main()
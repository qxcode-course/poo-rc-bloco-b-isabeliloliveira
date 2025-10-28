class Grafite:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__size = size
        self.__thickness = thickness
        self.__hardness = hardness
    
    def usagePerSheet(self):
        if self.__hardness == "HB":
            return 1
        
        elif self.__hardness == "2B":
            return 2
        
        elif self.__hardness == "4B":
            return 4
        
        elif self.__hardness == "6B":
            return 6
        
        else:
            return 0
        
    def get_thinckness(self):
        return self.__thickness
    
    def get_hardness(self):
        return self.__hardness
    
    def get_size(self):
        return self.__size
    
    def set_size(self, size: int):
        self.__size = size

    def __str__(self):
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"
    
class Lapiseira:
    def __init__(self):
        self.__tip = Grafite | None = None
        self.__thickness: float = 0
        
    def set_thickness(self, espessura: float):
        self.__thickness = espessura
        
    def get_tip(self):
        return self.__tip
    
    def inserir(self, grafite: Grafite):
        if self.__tip !=None:
            print("fail: ja existe grafite")
            return
        
        if grafite.get_thickness() != self.__thickness:
            print("fail: calibre incompativel")
            return
        self.__tip = grafite
    
    def remover(self) -> Grafite | None:
        aux = self.__tip
        self.__tip = None
        return aux
        
    def writePage(self):
        if self.__tip is None:
            print("fail: nao existe grafite")
            return
        size = self.__tip.get_size()
        cost = self.__tip.usagePerSheet()
        result=size-cost
        
        if size<=10:
            print("fail: tamanho insuficiente")
            return
        if result<10:
            print("fail: folha incompleta")
            self.__tip.set_size(10)
            return

        self.__tip.set_size(result)
        
    def __str__(self):
        grafite = self.__tip if self.__tip != None else "null"
        return f"calibre: {self.__thickeness}, grafite: {grafite}"
    
    
    
def main():
    lapiseira = Lapiseira()
    while True:
        line = input()
        print("$"+line)
        args = line.split(" ")
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(lapiseira)
        
        elif args[0]=="insert":
            thickness = args[1]
            hardness = args [2]
            size = args[3]
            grafite = Grafite(float(thickness), hardness, int(size))
        elif args [0] =="init":
            lapiseira.set_thickness(float(args[1]))
        
        
main()
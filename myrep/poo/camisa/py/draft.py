class Camisa:
    def __init__(self):
        self.__tamanho: str = ""
        
    
    def get_tamanho(self):
        return self.__tamanho
    
    def set_tamanho(self, tamanho: str):
        if tamanho.upper()!="PP" and tamanho.upper()!="P" and tamanho.upper()!="M" and tamanho.upper()!="G" and tamanho.upper()!="GG" and tamanho.upper()!="XG":
            print("fail: Tamanho de camisa invalido - Tamanhos permitidos: PP, P, M, G, GG e XG")
            return
        self.__tamanho = tamanho
        
def main():
    camisa = Camisa()
    while camisa.get_tamanho()=="":
        print("Digite seu tamanho de roupa")
        tamanho = input() 
        camisa.set_tamanho(tamanho) 
        
    print("Parabens, você comprou uma roupa tamanho", camisa.get_tamanho().upper())
    

main()
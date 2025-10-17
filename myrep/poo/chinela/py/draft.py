class Chinela:
    def __init__(self):
        self.__tamanho: int = 0 
        
    def set_tamanho(self, t: int) -> bool:
        if t<20 or t>50 and t %2 != 0:
            print("fail: tamanho invalido")
            return
        self.__tamanho = t

    def get_tamanho(self):
        return self.__tamanho
    
def main():
    chinela: Chinela = Chinela()
    while chinela.get_tamanho() == 0:
        print("Digite seu tamanho de chinela")
        tamanho = int(input()) 
        chinela.set_tamanho(tamanho)  

    print("Parabens, você comprou uma chinela tamanho", chinela.get_tamanho())
        



main()
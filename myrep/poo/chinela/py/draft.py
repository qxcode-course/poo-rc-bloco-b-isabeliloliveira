class Chinela:
    def __init__(self, tamanho: int):
        self.tamanho: int = 0 
        
    def __str__(self) -> str:
        return f"Parabens, você comprou uma chinela tamanho: {self.tamanho}"

    def set_tamanho(self, t: int) -> bool:
        if t>=20 and t<=50 and t %2==0:
            self.tamanho=t
            return
        else:
            print()

    def get_tamanho(self):
        return self.tamanho
    
def main():
    chinela = Chinela()
    while chinela.getTamanho() == 0:
        print("Digite seu tamanho de chinela")
        tamanho = int(input()) 
        chinela.set_tamanho(valor)  

    print("Parabens, você comprou uma chinela tamanho", chinela.getTamanho())
        



main()
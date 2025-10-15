class Chinela:
    def __init__(self, tamanho: int):
        self.tamanho: int = 0 
        
    def _str_(self) -> str:
        return f"Parabens, você comprou uma chinela tamanho: {self.tamanho}"

    def set_tamanho(self, t: int) -> bool:
        if t>=20 and t<=50 and t %2==0:
            self.tamanho=t
            return
        else:
            print()

    def get_tamanho(self):
        return self.__tamanho
    
def main():
    chinela = Chinela()
    
        



main()
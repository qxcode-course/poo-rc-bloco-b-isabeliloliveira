class Chinela:
    def __init__(self, tamanho: int):
        self.tamanho: int = 0 
        

    def set_tamanho(self):
        # self.min_tam: int = 20
        # self.max_tam: int = 50


def main():
    chinela: Chinela=Chinela(" ")
    while True:
        line: str=input()
        args: list[str]= line.split(" ") 



main()
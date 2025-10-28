class Notebook:
    def __init__(self, cap: int):
        self.__potencia = cap
    
    def get_potencia(self):
        return self.__potencia
    
    def __str__(self):
        return f"Potencia: {self.__potencia}"
    
class Bateria:
    def __init__(self, cap: int):
        self.__carga = cap
        self.__cap=cap
    
    def get_carga(self):
        return self.__carga
    
    def get_cap(self):
        return self.__cap
    
    def desc(self, temp: int):
        self.__carga-=temp
        if self.carga>self.__cap:
            self.__carga = 0
            
        
            
    
    
    
class Carregador:
    
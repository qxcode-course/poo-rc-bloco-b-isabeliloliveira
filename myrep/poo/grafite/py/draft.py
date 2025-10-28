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
        self.tip = None
        
    def hasGrafite(self):
        if self.__size!=None:
            return True
    
        
    def __str__(self):
        return f"calibre: {self.__thickeness}, grafite: [{}:{}:{}]"
    
    
    
def main():
    
    
main()
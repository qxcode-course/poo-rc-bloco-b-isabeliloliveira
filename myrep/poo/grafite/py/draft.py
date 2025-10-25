class Grafite:
    def __init__(self):
        self.__size: int = 0
        self.thickness: int
        self.hardness: str
        
class Lapiseira:
    def __init__(self):
        self.tip = None
        
    def hasGrafite(self):
        if self.__size!=None:
            return True
        
    def usagePerSheet(self):
        
    def __str__(self):
        return f"calibre: {}, grafite: [{}:{}:{}]"
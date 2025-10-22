class Grafite:
    def __init__(self):
        self.__size: int = 0
        
        
class Lapiseira:
    def __init__(self):
        self.tip = None
        
    def hasGrafite(self):
        if self.__size!=None:
            return True
        
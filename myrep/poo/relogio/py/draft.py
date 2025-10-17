class Watch:
    def __init__(self):
        self.__hora : int = 0
        self.__minuto: int = 0
        self.__segundo: int = 0

    def getHora(self):
        return self.__hora
    
    def getMinuto(self):
        return self.__minuto

    def getSegundo(self):
        return self.__segundo

    def __str__(self) -> str:
        return f"{self.getHora():02}:{self.getMinuto():02}:{self.getSegundo():02}"

    def setHora(self, hora: int):
        if hora <0 or hora>23:
            print("fail: hora invalida")
            return
        self.__hora=hora

    def setMinuto(self, minuto: int):
        if minuto <0 or minuto>59:
            print("fail: minuto invalido")
            return
        self.__minuto=minuto

    
    def setSegundo(self, segundo: int):
        if segundo <0 or segundo>59:
            print("fail: segundo invalido")
            return
        self.__segundo=segundo


    def s_hora(self, hora: int):
        if hora <0 or hora>23:
            print("fail: hora invalida")
            self.__hora=0
            return
        self.__hora=hora

    def s_minuto(self, minuto: int):
        if minuto<0 or minuto>59:
            print("fail: minuto invalido")
            self.__minuto=0
            return
        self.__minuto= minuto

    def s_segundo(self, segundo: int):
        if segundo<0 or segundo>59:
            print("fail: segundo invalido")
            self.__segundo=0
            return
        self.__segundo= segundo

    def seg_pular1(self):
        if self.getSegundo() == 59:
            self.setSegundo(0)
            if self.getMinuto() == 59:
                self.setMinuto(0)
                if self.getHora() == 23:
                    self.setHora(0)
                else:
                    self.setHora(self.getHora()+1)
                    
            else:
                self.setMinuto(self.getMinuto()+1)
        
        else:
            self.setSegundo(self.getSegundo()+1)


def main():
    watch= Watch()
    
    
    while True:
        line: str=input()
        print("$" +line)
        
        args: list[str] = line.split(" ")
        
        if args[0]=="end":
            break
        
        elif args[0]=="show":
            print(watch)  
        
        elif args [0] == "set":
            args[1]=watch.setHora(int(args[1]))
            args[2]=watch.setMinuto(int(args[2]))
            args[3]=watch.setSegundo(int(args[3]))
            
        elif args [0] == "init":
            args[1]=watch.s_hora(int(args[1]))
            args[2]=watch.s_minuto(int(args[2]))
            args[3]=watch.s_segundo(int(args[3]))
        
        elif args[0] == "next":
            watch.seg_pular1()

main()

            
        
class ClassConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None
        
    def setPropiedadPrivada(self, valor):
        self.__propiedad_privada = valor
        
    def getPropiedadPrivada(self):
        return self.__propiedad_privada
        
    #Esta función es un getter y setter en una sola función
    #El primero es un getter, el segundo, setter.
    def propiedadPrivada(self, valor=None):
        if valor == None:
            return self.__propiedad_privada
        else:
            self.__propiedad_privada = valor
    
    def __str__(self):
        return "ClaseConGetterySetter con propiedadPrivada -> {}".format(self.__propiedad_privada)
    
if __name__ == "__main__":
    c = ClassConGetterySetter()

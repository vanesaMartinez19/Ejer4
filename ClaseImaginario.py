class fraccion:
    __numerador = 0
    __denominador = 0
    __op = ''

    def __init__(self, num, den, op):
        self.__numerador : int = num
        if den == 0:
            raise ZeroDivisionError("El denominador no puede ser 0")
        self.__denominador: int = den
        self.__op = op
    
    def __str__(self):
        return ("{} + {}".format(self.__numerador, self.__denominador)) 

    def __add__(self, other):
        num = (self.__numerador + other.__numerador) 
        den = (other.__denominador + self.__denominador)
        if self.__op == '+':
            return ('{}+{}i'.format(num, den)) 
        else:
            return ('{}-{}i'.format(num, den))

    def __sub__(self , other):
        num = (self.__numerador - other.__numerador) 
        den = (other.__denominador - self.__denominador)
        if self.__op == '+':
            return ('{}+{}i'.format(num, den)) 
        else:
            return ('{}-{}i'.format(num, den))
    
    def __mul__(self , other):
        num = self.__numerador * other.__numerador
        den = self.__denominador * other.__denominador
        if self.__op == '+':
            return ('{}+{}i'.format(num, den)) 
        else:
            return ('{}-{}i'.format(num, den))
    
    def __truediv__(self , other):
        
        if other.__numerador == 0 and other.__denominador == 0:
            raise ZeroDivisionError("Division por cero")
        
        num = self.__numerador / other.__numerador
        den = self.__denominador / other.__denominador
        if self.__op == '+':
            return ('{}+{}i'.format(num, den)) 
        else:
            return ('{}-{}i'.format(num, den))

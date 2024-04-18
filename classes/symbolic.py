class Math_Symb:
    
    @staticmethod
    def check_attr(self_var:int,value:int) -> bool:
        if self_var == value:
            return True
        else:
            return False
    
    def __init__(self,coefficient:float, symbol:str, index:float) -> None:
        self.coefficient = coefficient
        self.symbol = symbol
        self.index = index
    
    def __add__(self, other):
        if self.symbol == other.symbol and self.index == other.index:
            return Math_Symb(self.coefficient + other.coefficient, self.symbol, self.index)
        else:
            return f'{Math_Symb(self.coefficient, self.symbol, self.index)} + {Math_Symb(other.coefficient, other.symbol, other.index)}'
    
    def __repr__(self) -> str:
        if self.coefficient == 0:
            return ''
        elif self.index == 0:
            return f'{self.coefficient}'
        elif self.coefficient == 1 and self.index == 1:
            return f'{self.symbol}'
        elif self.index == 1:
            return f'{self.coefficient}{self.symbol}'
        else:
            return f'{self.coefficient}{self.symbol}^{self.index}'
            
        
        
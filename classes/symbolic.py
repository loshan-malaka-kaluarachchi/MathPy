class Math_Symb:
    
    def __init__(self,coefficient:float, symbol:str, index:float) -> None:
        self.coefficient = coefficient
        self.symbol = symbol
        self.index = index
    
    def __add__(self, other):
        return self.coefficient + other.coefficient
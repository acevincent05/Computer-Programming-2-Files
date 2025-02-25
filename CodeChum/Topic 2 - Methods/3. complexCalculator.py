class ComplexCalculator:
    def get_sum(self, number1: int, number2: int) -> float:
        sum = number1 + number2
        return sum
        
    def get_difference(self, number1: int, number2: int) -> float:
        diff = number1 - number2
        return diff
        
    def get_product(self, number1: int, number2: int) -> float:
        product = number1 * number2
        return product
        
    def get_square_root(self, number: int) -> float:
        sqr =  number**.5
        if number > 0:
            return sqr
        else:
            return 0
    
    def get_quotient(self, number1: int, number2: int) -> float:
        try: 
            quo = number1/number2
            return quo 
        except:
            return 0
            
    def get_factorial(self, number: int) -> int:
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        return fact
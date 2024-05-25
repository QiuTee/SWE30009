class Calculation:
    def __init__(self):
        self.symbols = ['+', '-', '*', "/"]

    def original_program(self, A, B):
        A = A - B
        return A * 2

    def operator1(self, symbol, a, b):
        if symbol == '+':
            return a + b
        elif symbol == '-':
            return a - b
        elif symbol == '*':
            return a * b
        else:
            return a / b

    def operator2(self, symbol, c):
        if symbol == '+':
            return c + 2
        elif symbol == '-':
            return c - 2
        elif symbol == '*':
            return c * 2
        else:
            return c / 2

    def calculate(self, symbol1, symbol2, a, b):
        c = self.operator1(symbol1, a, b)
        result = self.operator2(symbol2, c)
        return result

    def checkResultValid(self, value, a, b):
        original_result = self.original_program(a, b)
        for symbol1 in self.symbols:
            for symbol2 in self.symbols:
                if symbol1 == '-' and symbol2 == '*':
                    continue
                result = self.calculate(symbol1, symbol2, a, b)
                if original_result == result:
                    value[(a, symbol1, symbol2 , original_result)] = result
        
        return value


if __name__ == "__main__":
    calculation = Calculation()
    value = {}
    for i in range(-1000, 1001):
        calculation.checkResultValid(value, i, 1)

    for val , result in value.items() : 
        print(f"Original result: {val[3]} ")
        print(f"Value of A: {val[0]}")
        print(f"Symbol: {val[1:3]}")
        print(f"Result: {result} \n")
        
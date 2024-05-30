class Solution(object):
    def __init__(self):
        self.signs = ['+', '-', '*', "/"]

    # Run the original program (correct case) - returns the correct result  
    def original_program(self, A, B):
        A = A - B
        return A * 2

    # Possible incorrect operator cases with "A = A - B ". 
    # Returns the value of the first operation between a and b with any incorrect operators occurring      
    def incorrect_case1(self, sign, a, b):
        if sign == '+':
            return a + b
        elif sign == '-':
            return a - b
        elif sign == '*':
            return a * b
        else:
            return a / b
        
    # Possible incorrect operator cases with " C = A * 2 ". 
    # Returns the value of the second operation (with c) with any incorrect operators occurring
    def incorrect_case2(self, sign, c):
        if sign == '+':
            return c + 2
        elif sign == '-':
            return c - 2
        elif sign == '*':
            return c * 2
        else:
            return c / 2
        
    # Calculate results based on the use of incorrect operators
    def calculate(self, sign1, sign2, a, b):
        c = self.incorrect_case1(sign1, a, b)
        result = self.incorrect_case2(sign2, c)
        return result

    # Perform calculations and check the results of operator error cases with the results of the original program
    def checkResultValid(self, value, a, b):
        original_result = self.original_program(a, b)
        # use a loop to iterate through all possible erroneous operators in the program 
        for sign1 in self.signs:
            for sign2 in self.signs:
                # Ignore the case if you sign "-" with "*" at the same time because that is the case the program provides 
                if sign1 == '-' and sign2 == '*':
                    continue
                result = self.calculate(sign1, sign2, a, b)
                # Check whether the results of the test are equal to the results of the original program. If it means this case did not achieve the testing goal 
                if original_result == result:
                    # if equal save information of value a , original value, sign1 , sign2 into "value" dictionary 
                    value[(a, sign1, sign2 , original_result)] = result
        
        return value


if __name__ == "__main__":
    solution = Solution()
    value = {}
    # iterate through A values ​​from -1000 to 1000 with B = 1 to find A values ​​that do not achieve the testing goal 
    for i in range(-1000, 1001):
        solution.checkResultValid(value, i, 1)

    for val , result in value.items() : 
        correct_result_str = f"{val[3]:.2f}".rstrip('0').rstrip('.')  
        incorrect_result_str = f"{result:.2f}".rstrip('0').rstrip('.')  
        # prints the value of A , the result of true and false and the false operators used 
        print(f"Result of the correct case: {correct_result_str}, Value of A: {val[0]}, Incorrect operators: {val[1:3]}, Result of the incorrect case: {incorrect_result_str} \n")


        
class Calculator:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def perform_calculation(self):
        if self.operator == '+':
            return self.num1 + self.num2
        elif self.operator == '-':
            return self.num1 - self.num2
        elif self.operator == '*':
            return self.num1 * self.num2
        elif self.operator == '/':
            if self.num2 != 0:
                return self.num1 / self.num2
            else:
                return "Error: Division by zero"
        elif self.operator == '%':
            if self.num2 != 0:
                return self.num1 % self.num2
            else:
                return "Error: Modulo by zero"
        elif self.operator == '^':
            return self.num1 ** self.num2
        else:
            return "Invalid operator. Please enter one of the supported operators: +, -, /, *, %, ^"


if __name__ == "__main__":
    print("Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, /, *, %, ^): ")

    calculator = Calculator(num1, num2, operator)
    result = calculator.perform_calculation()

    if isinstance(result, str):
        print(result)
    else:
        print(f"Result: {result}")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Addition:{add(num1, num2)}")
print(f"Subtraction:{sub(num1, num2)}")
print(f"Multiplication:{mul(num1, num2)}")
print(f"Division:{div (num1, num2):.2f}")
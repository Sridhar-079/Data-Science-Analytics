# WEEK 1 – PYTHON BASICS

# Temperature Converter
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)

# Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)

# Average Temperature
temps = [30, 32, 29, 35, 31]
print("Average temperature:", sum(temps)/len(temps))

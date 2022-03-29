def calculator(a, b, c):
    if c == '+':
        x = a + b
    elif c == '-':
        x = a - b
    elif c == '*':
        x = a * b
    elif c == '/':
        x = a / b
    else:
        x = 'Wrong action. Please try again'
    return x

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = input('Enter action (+, -, *, /) ')

print(calculator(a,b,c))
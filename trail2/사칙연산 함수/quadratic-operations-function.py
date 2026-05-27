a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def plus(a, c):
    return a + c
def minus(a, c):
    return a - c
def divide(a, c):
    return a // c
def multiple(a, c):
    return a * c

def calculator(a,o,c):
    calculator_options = ['-','+','*','/']
    result = 0
    if o in calculator_options:
        if o == '+':
            result = plus(a,c)
        elif o == '-':
            result = minus(a,c)
        elif o == '*':
            result = multiple(a,c)
        elif o == '/':
            result = divide(a,c)
    else:
        print(False)
        return
    print(f'{a} {o} {c} = {result}')

calculator(a,o,c)
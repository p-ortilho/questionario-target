def fibonacci(n):
    a, b = 0, 1

    while b <= n:
        if b == n:
            print(f'{n} pertence a sequência de Fibonacci.')
        
        a, b = b, a + b
    return f'{n} não pertence a sequência de Fibonacci!'

valor = fibonacci(4)
print(valor)
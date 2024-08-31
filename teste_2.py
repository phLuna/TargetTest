number = int(input('Insira um número: '))
fibonacci_sequence = [0, 1]

while fibonacci_sequence[-1] < number:
    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

if number in fibonacci_sequence:
    print(f'{number} pertence à sequência de Fibonacci!')
else:
    print(f'{number} não pertence à sequência de Fibonacci.')
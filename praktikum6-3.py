# Program 3
print("Program 3: Menampilkan urutan nilai dari Fibonacci")

def fibonacci(n):
    fib_sequence = [1, 1]
    for i in range(2, n):
        next_value = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_value)
    return fib_sequence

n = 10

fib_sequence = fibonacci(n)
for num in fib_sequence:
    print(num)
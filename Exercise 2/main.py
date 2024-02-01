import time
import random

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = random.randint(15, 35)

start_time = time.time()
result = fibonacci(n)
end_time = time.time()

print(f"fib({n}): {result}")
print(f"fib({n}) took {end_time - start_time} seconds")

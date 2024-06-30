"""
sequence = []
first_num = 0
second_num = 1
numsum = first_num + second_num

sequence.append(first_num)
sequence.append(second_num)
sequence.append(numsum)

while len(sequence) <= 10:

    first_num = numsum
    second_num = second_num + numsum
    numsum = first_num + second_num
                
    sequence.append(second_num)
    sequence.append(numsum) 

print(sequence)
"""

# Also:

first_num = 0
second_num = 1

while second_num <= 1597:
    print (first_num, second_num, end=" ")
    first_num = first_num + second_num
    second_num = first_num + second_num

# Also

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

primeros_10_fibonacci = fibonacci(10)
print(primeros_10_fibonacci)
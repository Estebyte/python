def increment(x):
    return x + 1

def high_order_function(x, func):
    return x + func(x)

result = high_order_function(10, increment)
# 10 + (10 + 1)
print(result)

increment_2 = lambda x: x + 1
high_order_function_2 = lambda x, func: x + func(x)
result_2 = high_order_function_2(10, increment_2 )
print(result_2)

result_3 = high_order_function_2(10, lambda x: x + 2)
print(result_3)
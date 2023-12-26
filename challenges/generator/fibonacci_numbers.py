def gen_fibonacci_numbers(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for i in gen_fibonacci_numbers(5):
    print(i)

# Будет напечатано
# 1
# 1
# 2
# 3
# 5

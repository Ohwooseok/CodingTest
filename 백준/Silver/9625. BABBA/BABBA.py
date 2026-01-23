K = int(input())

a, b = 1, 0  # k=0
for _ in range(K):
    a, b = b, a + b

print(a, b)
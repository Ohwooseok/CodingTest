def solution(n, tops):
    MOD = 10007

    A = 1
    B = 2 + tops[0]
    
    for i in range(1, n):
        prevA, prevB = A, B
        A = (prevA + prevB) % MOD
        B = ((1+tops[i]) * prevA + (2+tops[i]) * prevB) % MOD

    return (A+B) % MOD

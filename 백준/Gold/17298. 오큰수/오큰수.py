n = int(input())
oh = list(map(int, input().split()))
stack = []

answer = [-1] * n

for i in range(n):

    while stack and oh[stack[-1]] < oh[i]:
        idx = stack.pop()
        answer[idx] = oh[i]

    stack.append(i)

print(' '.join(map(str, answer)))

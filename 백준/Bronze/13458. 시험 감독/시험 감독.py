test_place = int(input())
test_people = list(map(int, input().split()))
first, second = map(int, input().split())
main = 0

for i in range(test_place):
    current = test_people[i]
    if current - first <= 0:
        main += 1
        continue
    else:
        main += 1
        current = current-first
        main += (current + second - 1) // second



print(main)
import heapq
import sys
import io


n = int(input())

people = [tuple(map(int, input().split())) for _ in range(n)]

people.sort(key = lambda x: x[0])
ocuup = [] # 사용중인 힙
available = [] # 비어있는 좌석 힙
seat_count = 0
usage = [0] * (n+1)

for P, Q in people:

    while ocuup and ocuup[0][0] <= P:
        _, seat_id = heapq.heappop(ocuup)
        heapq.heappush(available, seat_id)

    if available:
        seat_id = heapq.heappop(available)
    else:
        seat_count += 1
        seat_id = seat_count

    usage[seat_id] += 1

    heapq.heappush(ocuup, (Q, seat_id))

print(seat_count)
print(*usage[1:seat_count+1])
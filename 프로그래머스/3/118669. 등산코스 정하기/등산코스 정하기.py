import heapq  # 최소 힙(우선순위 큐) 구현을 위한 모듈

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]  # 인접 리스트(1~n까지 사용)

    for i, j, w in paths:               # 등산로 정보 반복
        graph[i].append((j, w))         # i → j 경로 추가
        graph[j].append((i, w))         # j → i 경로 추가 (양방향)

    gate_set = set(gates)               # 출입구를 빠르게 확인하기 위한 set
    summit_set = set(summits)           # 산봉우리도 set으로 변환 (in 연산 빠르게)

    INF = float('inf')                  # 무한대 값 (초기 거리 대체)
    intensity = [INF] * (n + 1)         # 각 지점까지의 최소 intensity 저장
    heap = []                           # 우선순위 큐 (최소 intensity 기준)

    # 모든 출입구를 다익스트라의 시작점으로 넣기
    for g in gates:
        intensity[g] = 0                # 출입구의 intensity는 0
        heapq.heappush(heap, (0, g))    # (intensity, 노드번호) 형태로 push

    # 다익스트라 시작
    while heap:
        cur_intensity, now = heapq.heappop(heap)  # intensity가 가장 낮은 노드 pop

        if intensity[now] < cur_intensity:        # 이미 더 좋은 경로로 방문한 적 있으면 스킵
            continue

        if now in summit_set:                     # 산봉우리면 더 이상 이동 불가 (끝점이므로)
            continue

        for next, cost in graph[now]:             # 인접 노드 순회
            new_intensity = max(cur_intensity, cost)  # 지금 경로에서의 최대 가중치 계산

            if intensity[next] > new_intensity:       # 더 낮은 intensity 경로 발견 시 갱신
                intensity[next] = new_intensity        # 값 업데이트
                heapq.heappush(heap, (new_intensity, next))  # 다음 노드 탐색 추가

    # 모든 산봉우리 중 최소 intensity 찾기
    answer_summit = 0
    answer_intensity = INF

    for s in sorted(summits):                 # 번호가 낮은 산봉우리부터 확인
        if intensity[s] < answer_intensity:   # 더 낮은 intensity라면 갱신
            answer_summit = s                 # 산봉우리 번호 저장
            answer_intensity = intensity[s]   # intensity 값 저장

    return [answer_summit, answer_intensity]  # [산봉우리 번호, 최소 intensity] 반환

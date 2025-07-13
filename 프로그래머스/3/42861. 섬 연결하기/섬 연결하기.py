def solution(n, costs):
    # 비용을 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])
    
    # 부모 노드 초기화
    parent = [i for i in range(n)]
    
    # Find 함수 (부모 찾기)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]
    
    # Union 함수 (합치기)
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False
    
    total_cost = 0
    for a, b, cost in costs:
        if union(a, b):  # 사이클이 생기지 않으면 연결
            total_cost += cost
    
    return total_cost

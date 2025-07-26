def solution(n, s, a, b, fares):
    
    # 지점의 개수 n, 출발지점을 나타내는 s, A의 도착지점을 나타내는 a, B의 도착지점을 나타내는 b, 지점 사이의 예상 택시요금을 나타내는 fares가 매개변수로 주어집니다.
    
    INF = float('inf')
    
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0
        
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    
    mintotal = INF
    for k in range(1, n+1):
        mini = graph[s][k] + graph[k][a] + graph[k][b]
        if mini < mintotal:
            mintotal = mini

    return mintotal
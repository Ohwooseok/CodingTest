import copy
from collections import defaultdict

def solution(info, edges):
    
    tree = defaultdict(list)
    
    for mom, sun in edges:
        tree[mom].append(sun)
    
    max_sheep = 0
    
    def dfs(node, sheep, wolf, next_nodes):
        nonlocal max_sheep
        
        if info[node] != 0:
            wolf += 1
        else:
            sheep += 1
        
        
        if wolf >= sheep:
            return
        
        max_sheep = max(sheep, max_sheep)
        
        candi = copy.deepcopy(next_nodes)
        candi.remove(node)
        candi += tree[node]
        
        for next_node in candi:
            dfs(next_node, sheep, wolf, candi)
    
    dfs(0,0,0,[0])
    return max_sheep
import sys
sys.setrecursionlimit(10000)
def solution(nodeinfo):
    
    
    nodes = [(x,y,i+1) for i, (x,y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda x :(-x[1], x[0]))
    
    class Node:
        def __init__(self, x, y, idx):
            self.x = x
            self.y = y
            self.idx = idx
            self.left = None
            self.right = None
    
    
    def insert(parent, child):
        # 자식이 부모보다 작으면 부모의 왼쪽으로
        if child.x < parent.x:
            if parent.left is None:
                parent.left = child
            else:
                insert(parent.left, child)
        else:
            # 부모의 오른쪽이 비어있으면 오른쪽에 삽입
            if parent.right is None:
                parent.right = child
            else:
                insert(parent.right, child)
    
    root = Node(*nodes[0])
    for node in nodes[1:]:
        insert(root, Node(*node))
    
    preorder= []
    def pre(node):
        if node:
            preorder.append(node.idx)
            pre(node.left)
            pre(node.right)
    postorder=[]
    def post(node):
        if node:
            post(node.left)
            post(node.right)
            postorder.append(node.idx)
        
    pre(root)
    post(root)
    
    return [preorder,postorder]
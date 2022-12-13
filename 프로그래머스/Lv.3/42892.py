import sys
sys.setrecursionlimit(10 ** 6)

preorder_list = []
postorder_list = []

def preorder(nodeinfo):
    if not nodeinfo:
        return
    root = nodeinfo[0][0]
    preorder_list.append(nodeinfo[0][2])
    left, right = [], []
    for i in range(1, len(nodeinfo)):
        if nodeinfo[i][0] < root:
            left.append(nodeinfo[i])
        else:
            right.append(nodeinfo[i])
    preorder(left)
    preorder(right)

def postorder(nodeinfo):
    if not nodeinfo:
        return
    root = nodeinfo[0][0]
    left, right = [], []
    for i in range(1, len(nodeinfo)):
        if nodeinfo[i][0] < root:
            left.append(nodeinfo[i])
        else:
            right.append(nodeinfo[i])

    postorder(left)
    postorder(right)
    postorder_list.append(nodeinfo[0][2])

def solution(nodeinfo):
    answer = []
    nodeinfo = [(b[0], b[1], a + 1) for a, b in enumerate(nodeinfo)]
    nodeinfo.sort(key = lambda x: (-x[1], x[0]))

    preorder(nodeinfo)
    answer.append(preorder_list)

    postorder(nodeinfo)
    answer.append(postorder_list)
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
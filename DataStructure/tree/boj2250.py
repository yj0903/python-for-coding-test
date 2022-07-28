# boj2250 트리의 높이와 너비 (골드2)
import sys

class Node:
    def __init__(self, data, left_node, right_node):
        self.parent = -1
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 중위 순위 함수 생성. level_list 유의
def inorder(level, node):
    global level_list
    # left
    if node.left_node != -1:
        inorder(level + 1, tree[node.left_node])
    # middle
    level_list.append(level) # 출력 되는 값의 레벨을 순서대로 배열에 담는다
    # right
    if node.right_node != -1:
        inorder(level + 1, tree[node.right_node])
    return level_list

# 변수 선언
number = int(input())
tree = {}
root = -1
level_list = list()  # 전역변수 선언, 각각의 레벨이 담길 리스트

# 트리 초기화(선언이 되어 있어야 아래 parent에 값대입 가능함..)
for i in range(1, number + 1):
    tree[i] = Node(i, -1, -1)

# 입력받아 트리에 넣기, parent 유의 (parent가 -1이면 루트)
for i in range(number):
    data, left_node, right_node = list(map(int, sys.stdin.readline().split()))
    tree[data].left_node = left_node
    tree[data].right_node = right_node
    if left_node != -1:
        tree[left_node].parent = data
    if right_node != -1:
        tree[right_node].parent = data
# 트리에 root 노드 반환
for i in range(1, number + 1):
    if tree[i].parent == -1:
        root = i

result = inorder(1, tree[root])
result_reverse = list(reversed(result))
max_width = 0
level_val = 0

# 앞에서 찾고, reverse해서 뒤에서 찾기
for i in range(1, max(result) + 1):
    min_val = result.index(i)
    max_val = len(result) - result_reverse.index(i)

    width = max_val - min_val
    if max_width < width:
        max_width = width
        level_val = i

# 결과 출력
print(level_val, max_width)

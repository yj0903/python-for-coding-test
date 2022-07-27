# boj2250 트리의 높이와 너비(골드2)

import sys


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


# dfs 알고리즘 inorder (left > self > right)

def in_order(node):
    #  좌
    if node.left is not None:
        in_order(tree[node.left])
    #  중
    print(node.data)
    #  우
    if node.right is not None:
        in_order(tree[node.right])


# 입력 받아 트리 생성
num = int(input())
tree = {}
start_data = -1

for i in range(num):
    data, left, right = list(map(int, sys.stdin.readline().split()))
    if left == -1:
        left = None
    elif right == -1:
        right = None
    if i == 0:
        start_data = data
    tree[data] = Node(data, left, right)

in_order(tree[start_data])

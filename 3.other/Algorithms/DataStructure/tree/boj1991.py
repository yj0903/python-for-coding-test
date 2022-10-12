# boj1991 Tree traversal

import sys


class Node:
    def __init__(self, data, leftNode, rightNode):
        self.data = data
        self.leftNode = leftNode
        self.rightNode = rightNode


# data - left - right 순서
def preOrder(node):
    print(node.data, end='')
    if node.leftNode != '.':
        preOrder(tree[node.leftNode])
    if node.rightNode != '.':
        preOrder(tree[node.rightNode])


# left - data - right 순서
def inOrder(node):
    if node.leftNode != '.':
        inOrder(tree[node.leftNode])
    print(node.data, end='')
    if node.rightNode != '.':
        inOrder(tree[node.rightNode])


# left- right - data 순서
def postOrder(node):
    if node.leftNode != '.':
        postOrder(tree[node.leftNode])
    if node.rightNode != '.':
        postOrder(tree[node.rightNode])
    print(node.data, end='')


# 입력 받아 트리 생성
num = int(input())
tree = {}

for i in range(num):
    data, leftNode, rightNode = list(sys.stdin.readline().split())
    tree[data] = Node(data, leftNode, rightNode)

# 전위
preOrder(tree['A'])
print()
# 중위
inOrder(tree['A'])
print()
# 후위
postOrder(tree['A'])

import os
import sys
import collections


class Node:
    def __init__(self, d):
        self.data = d


def build_tree(indexes):
    def f(x): return None if x == -1 else Node(x)
    children = {n.data: n for n in filter(None, sum(children, []))}
    nodes = {n.data: n for n in filter(None, sum(children, []))}
    nodes[1] = Node(1)
    for idx, child_pair in enumerate(children):
        nodes[idx+1].left = child_pair[0]
        nodes[idx+1].right = child_pair[1]
    return nodes[1]


def inorder(root):
    stack = []
    curr = root
    while stack or curr:
      if curr:
        stack.append(curr)
        curr = curr.left
      elif stack:
        curr = stack.pop()
        yield curr.data
        curr = curr.right

def swapNodes(indexes, queries):
  root = build_tree(indexes)
  for k in queries:
    h = 1
    q = collections.deque([root])
    while q:
      for _ in range(len(q)):
        node = q.popleft()
        if h % k == 0:
          node.left, node.right = node.right, node.left
        q += filter(None, (node.left, node.right))
      h += 1 # Height
    yield inorder(root)

# indexes = [[2,3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]]

# f = lambda x: None if x == -1 else Node(x)
# children = [list(map(f, x)) for x in indexes]
# print(children)
# print(sum(children, []))
# # sum(이중리스트, []) 이런식으로 합칠 수 있다.
# nodes = {n.data: n for n in filter(None, sum(children, []))}
# nodes[1] = Node(1)
# for idx, child_pair in enumerate(children):
#     nodes[idx+1].left = child_pair[0]
#     nodes[idx+1].right = child_pair[1]
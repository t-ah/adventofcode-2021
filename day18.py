import math
import json


class Node:
    def __init__(self, content=None, parent=None):
        self.parent = parent
        self.v = None
        self.left, self.right = None, None
        self.depth = parent.depth + 1 if parent else 0
        if content != None:
            if type(content) is list:
                self.left = Node(content[0], self)
                self.right = Node(content[1], self)
            else:
                self.v = content
    
    def to_str(self):
        return f"(v: {self.v}, l: {self.left.to_str() if self.left else None}, r: {self.right.to_str() if self.right else None})"

    def update_depth(self, parent_depth=-1):
        self.depth = parent_depth + 1
        if self.left != None:
            self.left.update_depth(self.depth)
        if self.right != None:
            self.right.update_depth(self.depth)

    def get_front(self):
        if self.left == None:
            return [self]
        return self.left.get_front() + self.right.get_front()

    def evaluate(self):
        if self.left:
            return 3 * self.left.evaluate() + 2 * self.right.evaluate()
        return self.v


def main():
    lines = read_input("day18.txt")
    tree = Node(lines[0])
    for line in lines[1:]:
        tree = add_trees(tree, Node(line))
        tree = reduce_tree(tree)
    print(tree.evaluate())

    mag_max = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j:
                continue
            mag = reduce_tree(add_trees(Node(lines[i]), Node(lines[j]))).evaluate()
            mag_max = max(mag_max, mag)
    print(mag_max)


def add_trees(t1, t2):
    tree = Node()
    tree.left = t1
    tree.right = t2
    t1.parent = tree
    t2.parent = tree
    tree.update_depth()
    return tree


def reduce_tree(tree):
    while True:
        if not explode(tree) and not split(tree):
            return tree


def explode(tree):
    front = tree.get_front()
    for i, leaf in enumerate(front):
        if leaf.depth == 5 and leaf.parent.right:
            partner_leaf = leaf.parent.right
            if i > 0:
                front[i - 1].v += leaf.v
            if i < len(front) - 2:
                front[i + 2].v += partner_leaf.v
            leaf.parent.v = 0
            leaf.parent.left = None
            leaf.parent.right = None
            return True
    return False


def split(tree):
    front = tree.get_front()
    for i, leaf in enumerate(front):
        if leaf.v >= 10:
            left, right = leaf.v // 2, math.ceil(leaf.v / 2)
            leaf.v = None
            leaf.left = Node(content=left, parent=leaf)
            leaf.right = Node(content=right, parent=leaf)
            return True
    return False


def read_input(file_name):
    with open(file_name, "r") as f:
        return [json.loads(x.strip()) for x in f.readlines()]


if __name__ == "__main__":
    main()
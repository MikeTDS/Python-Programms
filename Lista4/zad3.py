import random

class Node(object):
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

def generate_tree(n,vals):
    val = random.choice(vals)
    vals.pop(vals.index(val))
    if n==1:
        return Node(val,None,None)
    else:
        return Node(val,
                    generate_tree(n-1,vals),
                    generate_tree(n-1,vals))

def DFS(tree):
    yield tree.val
    if tree.left is not None:
        yield from DFS(tree.left)
    if tree.right is not None:
        yield from DFS(tree.right)

def BFS(tree):
    visited = []
    queue = []
    visited.append(tree)
    queue.append(tree)

    while queue:        
        s = queue.pop(0)
        if s is not None:
            yield s.val
            if s.left not in visited:
                visited.append(s.left)
                queue.append(s.left)
            if s.right not in visited:
                visited.append(s.right)
                queue.append(s.right)


def main():
    n = 3
    tree = generate_tree(n,list(range(1,pow(n,2))))
    print('DFS: ' + str(list(DFS(tree))))
    print('BFS: ' + str(list(BFS(tree))))

if __name__ == "__main__":
    main()
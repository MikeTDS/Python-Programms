import random

def gen_rand_tree(n,vals):
    val = random.choice(vals)
    vals.pop(vals.index(val))
    if n==1:
        return[val, None, None]
    else:
        return[
            val,
            gen_rand_tree(n-1,vals),
            gen_rand_tree(n-1,vals)
            ]

def DFS(tree):
    yield tree[0]
    for i in range(1,len(tree)):
        if tree[i] is not None:
            yield from DFS(tree[i])

def BFS(tree):
    visited = []
    queue = []
    visited.append(tree)
    queue.append(tree)

    while queue:        
        s = queue.pop(0)
        if s is not None:
            yield s[0]
            for n in range(1,len(s)):
                if s[n] not in visited:
                    visited.append(s[n])
                    queue.append(s[n])
def main():
    n = 4
    tree = gen_rand_tree(n,list(range(1,pow(2,n))))
    print(tree)
    print('DFS: ' + str(list(DFS(tree))))
    print('BFS: ' + str(list(BFS(tree))))
if __name__ == "__main__":
    main()
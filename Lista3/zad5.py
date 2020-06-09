def generate_subsets(array):
    res = [[]]
    for x in array:
        res += [sub+[x] for sub in res]
    return res

def generate_subsets_2(array):
    res = [[]]
    for x in array:   
        res += list(map(lambda sub: sub + [x], res))
    return res

def main():
    print(generate_subsets(['a','b','c']))
    print(generate_subsets_2([1,2,3]))

if __name__ == "__main__":
    main()
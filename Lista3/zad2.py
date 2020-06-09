def flatten(l):
    for x in l:
        if type(x) is list:
            yield from flatten(x)
        else:
            yield x

def main():
    l = [5,[6, [1, 3], 4], [2], [8, 9, [[10]]]]
    print(list(flatten(l)))
if __name__ == "__main__":
    main()
import random

def quick_sort(array):

    if len(array) < 2:
        return array
    pivot = array.pop(-1)

    return quick_sort([x for x in array if x < pivot]) \
    + [pivot] \
    + quick_sort([x for x in array if x >= pivot])

def quick_sort_2(array):

    if len(array) < 2:
        return array
    pivot = array.pop(-1)
    
    return quick_sort_2(list(filter(lambda x: x < pivot, array))) \
    + [pivot] \
    + quick_sort_2(list(filter(lambda x: x >= pivot, array)))

def main():
    print(quick_sort([random.randint(1,100) for i in range(10)]))
    print(quick_sort_2([random.randint(1,100) for i in range(10)]))

if __name__ == '__main__':
    main()
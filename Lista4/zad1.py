import time

def show_time(f):
    def my_func(*args,**kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        print(str(time.time()-start))
        return res
    return my_func

@show_time
def foo(n=10):
    for i in range(n):
        print(i, end=' ')
    print('')
    return n

def main():
    k = foo(1000000)

if __name__ == "__main__":
    main()



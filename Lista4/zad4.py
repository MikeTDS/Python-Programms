from inspect import getfullargspec
import math


class CustomFunction(object):
    def __init__(self, f):
        self.f = f
  
    def __call__(self, *args, **kwargs):
        f = FunctionsSet.get_set().get(self.f, *args)
        return f(*args, **kwargs)

class FunctionsSet(object):
    f_set = None

    def __init__(self):
        if self.f_set is None:
            FunctionsSet.f_set = self
            self.function_dict = dict()
            
    @staticmethod
    def get_set():
        if FunctionsSet.f_set is None:
            FunctionsSet()
        return FunctionsSet.f_set
    
    def add(self, f):
        self.function_dict[self.get_id(f)] = f
        return CustomFunction(f)
    
    def get(self, f, *args):
        return self.function_dict.get(self.get_id(f,args=args))

    def get_id(self, f, args=None):
        if args is None:
            args = getfullargspec(f).args
        return (f.__name__, len(args))

def overload(f):
    return FunctionsSet.get_set().add(f)

@overload
def norm(x,y):
    return math.sqrt(x*x + y*y)
  
@overload
def norm(x,y,z):
    return abs(x) + abs(y) + abs(z)

def main():
    print(f"norm(2,4) = {norm(2,4)}")
    print(f"norm(2,3,4) = {norm(2,3,4)}")

if __name__ == "__main__":
    main()
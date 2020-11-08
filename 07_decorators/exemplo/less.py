def decorator(func):
    def wrap(num):
        if num < 100:
            func()
            wrap.div = num/2
        else:
            return 'big to high'
    return wrap

@decorator
def numbers( ):
    print("Less than 100")

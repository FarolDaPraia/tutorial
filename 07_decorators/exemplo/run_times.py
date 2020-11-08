# creating a decorator that takes in parameters
def run_times(num):
    def wrap(func):
        for i in range(num):
            func( )
    return wrap

@run_times(4)
def sayHello( ):
    print("Hello!")

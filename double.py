def double(func):
    def wrapper():
        func()
        print("Let's try that again!")
        func()
    return wrapper

#To use the double decorator:

from double import double

@double
def my_func():
    print("Hello, world!")

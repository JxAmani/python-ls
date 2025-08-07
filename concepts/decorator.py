# Decorators.
#Extend or modify the behaviour of 
## functions or without changing their code
## CALLBACKS<-->

# def my_deco(func):
#     def wrapper():
#         print("Before function run")
#         func()
#         print("Function completed running")
#     return wrapper

# @my_deco
# def hello():
#     print("hello world")
# 
#my_deco(func=hello)()

# hello()

def my_deco(func):
    def wrapper():
        print("caling Hello World function")
        func()
        print("Finished calling Hello World ")

    return wrapper

@my_deco
def hello_world():
    print("Hello World")

hello_world()

@my_deco
def greet():
    print("Greetings from above")

greet()


def my_deco2(func):
    def wrapper():
        print("123")
        func()
        print("456")

    return wrapper

@my_deco2
def peace():
    print("peace")


peace()
import time

def time_fn(fn):
    def wrapper():
        start_time = time.time()  # record start time
        fn()  # run the function
        end_time = time.time()  # record end time
        print("Time taken to run counter function is", end_time - start_time)
    return wrapper  # return the wrapped function
@my_deco
@time_fn
def counter():
    for n in range(0, 100):  # fixed 0 instead of o
        print(n)

# Run the counter function
counter()



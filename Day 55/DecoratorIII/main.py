# Create a logging_decorator() which is going to log the name of the function that was called,
# the arguments it was given and finally the returned output.

def logging_decorator(function):
    def wrapper(*args):
        print(f"You called: {function.__name__}{args}")
        print(f"It returned: {function(*args)}")
    return wrapper


@logging_decorator
def multiply(a, b):
    return a * b


multiply(3, 4)

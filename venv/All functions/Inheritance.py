'''def hello(name = "Gopi"):
    print("Hello " + name)

    def greet():
        return  "This string is inside greet()"

    def welcome():
        return "this string is inside welcome"

    if name == "Gopi":
        return greet
    else:
        return welcome

x = hello()
#Assigning funtion to a variable
mynewgreet = hello
print(x())'''

'''def hello():
    return "hi Gopi"
def other(func):
    print("Hello")
    print(func())
other(hello)'''

def new_decorator(func):

    def wrap_function():
        print('CODE HERE BEFORE EXECUTING FUNCT')
        func()
        print('Function has been called')
    return wrap_function()

@new_decorator
def func_needs_decorator():
    print("This fucntion us in need of a decorator")

func_needs_decorator


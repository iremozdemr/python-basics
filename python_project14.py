def decorator_function(function):
    def inner_function():
        print("this is before function execution")
        function()
        print("this is after function execution")

    return inner_function

def function_to_be_used():
    print("function to be used")

function_to_be_used = decorator_function(function_to_be_used)

function_to_be_used()
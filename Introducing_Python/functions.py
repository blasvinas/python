#Shows how to use functions

def good():
    return ["Harry","Ron","Hermione"]
print(good())

get_odds = (number for number in range(10) if number % 2 != 0)
for number in get_odds:
    print(number)

def document_function(func):
    def new_function(*args, **kwargs):
        print(f"Funtion name: {func.__name__}")
        print(f"Function documentation: {func.__doc__}")
        return func(*args, **kwargs)
    return new_function

@document_function
def data(*args, **kwargs):
    'Print some data'
    print(args)
    print(kwargs)
data(1,2,3,4,5,month="May", day=15, year=1971)

def OopsException():
    try:
        x = 10
        y = 0
        z = x / y
    except:
        print("Caught in OopsException")
OopsException()

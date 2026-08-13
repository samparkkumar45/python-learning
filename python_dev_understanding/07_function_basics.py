#Function is a re-useable block of code.
#Function is a machine which take input and return output.
def hello_func():
    print('Hello!')
hello_func() #if we change something it take less time.
hello_func() 
hello_func() 
hello_func() 
print('Hello!') # in this the main problem if you want to change something it take more time
print('Hello!') #it allow us to put a specific function in single loctaion.
print('Hello!')
def hello_func():
    return 'Hello!' #when we execute a function it return this value.
print(hello_func())
print(hello_func().upper())
#Argument Passing
def hello_func(greeting):
    return '{} Function'.format(greeting)
print(hello_func('Hi')) #here you must required 1 positional argument: 'greeting'
def hello_func(greeting , name ):
    return '{} , {}'.format(greeting , name) # required positional arguments must come befor keywoard argument.
print(hello_func('Hi' , 'Sampark'))
def student_info(*arags, **kwargs): #it allow us to accept arbitrary number of positional and keywoard argument.
    print(arags) # using this when you don't know how much positional and keywoard argument you have.
    print(kwargs)
student_info("Math , Arts" , name = 'sampark' , age = 20) # here math and arts is an positional argument and name and age are keywoard argument. 
def student_info(*arags, **kwargs): #it allow us to accept arbitrary number of positional and keywoard argument.
    print(arags)
    print(kwargs)
courses = ['math' , 'Art']
info = {'name' : 'sampark' , 'age' : 20}
student_info(*courses , **info) # unpack our positional and keywoard argument.
# question
month_days = [0 , 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31]
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0)

def dayes_in_month(year , month):
    if not 1 <= month <=12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
print(is_leap(2020))
print(dayes_in_month(2020, 1))
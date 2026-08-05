message = """ hi my name is sampark and i currently 
study python and  also learn the basic of it.
"""
print(message)

message = "my name is sampark"
print(len(message))

message = "my name is sampark"
print(message[7:])

message = "my name is sampark"
print(message.replace("sampark" , "sam"))
print(message.lower())
print(message.upper())
print(message.count(' '))
print(message.find("name"))
print(message.find("hello"))
greeting = "Hello" 
name = "viewer"
message = greeting + ', ' + name + '. ' 'welcome!'
message = '{}, {}. welcome!.format(greeting, name)' # not working # {} in this we called is place holder.
message = f'{greeting}, {name.upper()}. welcome!' # python version above 3.06 the f string is working.
print(message)
print(dir(name)) # dir() gives all the method and attributes that we have acceses through the varible.
print(help(name)) # help() does't work in variables for use it we need string and class it self. 
print(help(str).lower()) # help() help us to find which which method and function we can use in string or class and it aslo give more information about specific method or function.


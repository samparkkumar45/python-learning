## 1 take your full name as input and print it.
name = input("enter your name:")
print("your name is:" , name)

## 2 find the legth of your name.
name1 = input("enter your name:")
print("your name length will be:" , len(name1))

## 3 print first character and last character of your name.
name2 = "sampark"
f = name2[0]
l = name2[6]

print("first character of your name is:" , f)
print("last character of your name is:" , l)

## 4 take a string and print it in uppercase.
collage_name = input("enter your collage name:")
collage_name.upper  # the upper is use for uppercase we can't use uppercase function
print("your collage name in uppercase will be:" , collage_name.upper())

## 5 take a string and print it in lowercase.
your_name = input("enter your name:")
your_name.lower
print("your name in lowercase will be:" , your_name.lower())

## 6 take a string and count how many spaces it has.
name = "sampark kumar"
c = ' '
for i in range (len(name)): # in range we can only take int value that why we use len(name).
    if c :                  # error: TypeError: 'str' object cannot be interpreted as an integer.
        print(name.count(c))
        break

## 7 take a string and replace one word with another.
str = "hi"
re = str.replace(("i") , ("h"))
print(re)

## 8 take a string and reverse it.
my_str = "sampark"
c = my_str[::-1] # use slicing concept.
for i in range (len(my_str)):
    if c:
        print(c)
        break

## 9 check if a string  is palindrome or not.
str = "pop"
d = str[0 : 3] == str[::-1]
for i in range (len(str)):
    if d:
        print("the number is palindrome:" , d)
    else:
        print("not palindrome")    

## 10 concatenate first name and last name with a space in between.
firstname = "sampark"
lastname = "kumar"
print((firstname) + (lastname))


 
    




     




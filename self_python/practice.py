# 1 take two numbers and print all arithmetic operations.
num1 = int(input("enter the value of num1: "))
num2 = int(input("enter the value of num2: "))
sum = num1 + num2 # Addition
sub = num1 - num2 # Subtraction
multi = num1 * num2 # Multiplication
div = num1 / num2 # Division
floor_div = num1 // num2 # Floor Division
modu = num1 % num2 # Modulus
print(sum , sub , multi , div , floor_div , modu)

# 2 take a string and check if it is palindrome.
str = "pop"
c = str[0 : 3] == str[::-1]
for i in range (len(str)):
    if c:
        print("the string is palindrome.")
    else:
        print("string is not palindrome.")

## 3 take age and print if eligible for vote and driving.
age = int(input("enter your age: "))
if(age >= 18):
    print("you are eligible for vote and driving.")
else:
    print("you are not eligible for vote and driving.")

## 4 take temperature in celsius and convert to fahrenheit.
temp = int(input("enter temperature in celsius."))
convert = temp * 9/5 + 32
print("the temperature in fahrenheit is: " , convert)

## 5 take a number and print factorial of that number.
num = int(input("enter your number: "))
factorial = 1
for i in range (1 , num+1):
    factorial = factorial*i

print("factorial = " , factorial)
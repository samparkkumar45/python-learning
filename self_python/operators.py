## 1 take two numbers and print their sum , difference , product and divison.
a = int(input("Enter the value of a:"))
b = int(input("enter the value of b:"))
sum = a+b
difference = a-b
product = a*b
division = a/b

print("the sum of two numbers are:" , sum)
print("the difference of two numbers are:" , difference)
print("the product of two numbers are:" , product)
print("the division of two numbers are:" , division)

## 2 print the remainder when a number is divided by another.
x = int(input("enter the value of x:"))
y = int(input("enter the value of y:"))
print("the remainder of two numbers are:" , x%y)

## 3 take two numbers and print the result of s ** m.
s = int(input("enter the value of s:"))
m = int(input("enter the value of m:"))
print("the value of a**b will be:" , s**m)

## 4 check if a number is even or odd.
num1 = int(input("enter the value of num1:"))
if (num1%2 == 0):
    print("the num1 is an even number:", num1)
else:
    print("the num1 is an odd number:" , num1)

## 5 check if number is positive , negative or zero.
num2 = int(input("enter the value of num2:"))
if(num2>0):
    print("the number is a positive number" , num2)
elif(num2<0):
    print("the number is a negative number" , num2)
else:
    print("the number is zero" , num2)

## 6 take two numbers and print the largest number.
num3 = int(input("enter the value of num3:"))
num4 = int(input("enter the value of num4:"))
if (num3 > num4):
    print("the num3 is the largest number:" , num3)
else:
    print("num4 is the largest number:" , num4)

## 7 take two numbers and print the smallest number.
num5 = int(input("enter the value of num5:"))
num6 = int(input("enter the value of num6:"))
if (num5 < num6):
    print("the num5 is the smallest number:" , num5)
else:
    print("num6 is the smallest number:" , num6)

## 8 check if a number is divisible by 7.
num7 = int(input("enter the value of num7:"))
if(num7 % 7 == 0):
    print("the number is divisible by 7")
else:
    print("number is not divisible by 7")

## 9 take a number and print its last digit.
num8 = int(input("enter the value of num8:"))                 ## 'int' object is not subscriptable
last_digit = num8 % 10
print("last digit:" , last_digit)    ## % this give the last number of digit

## 10 evalute the following expression (5 + 3 * 2 -4 / 2) and print the result.
exp = (5 + 3 * 2 - 4 / 2)
print("the result will be:" , exp)
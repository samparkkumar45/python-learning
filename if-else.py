## 1 take age as input and check if a person is eligible to vote (age>=18)
age = int(input("enter your age:"))
if (age>=18):
    print("you are eligible to vote")
else :
    print("you are not eligible")

## 2 take a number and check if it is positive , negative or zero.
num = int(input("enter a number:"))
if (num>0):
    print("the number is positive")
elif (num<0):
    print("the number is negative")
else:
    print("the number is zero")   

## 3 take a number and check if it is even or odd.
num1 = int(input("enter a number:"))
if(num1%2 == 0):
    print("the number is even")
else:
    print("the number is odd")

## 4 take two number and print the largest number.
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: " ))
if(num1>num2):
    print("the num1 is largest number")
else:
    print("the num2 is largest number")

## 5 take three numbers nd print the largest number.
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
if (num1>num2) & (num1>num3):
    print("the num1 is the largest number")
elif (num2>num1) & (num2>num3):
    print("the num2 is the largest number")
else:
    print("num3 is the largest number")

## 6 take a number and check if it is divisible by 5.
num = int(input("enter a number: "))
if (num % 5 == 0):
    print("the number is divisible by 5")
else:
    print("the number is not divisible by 5")

## 7 take marks as input and print the grade: A(90-100) , B(80-89) , C(70-79) , D(60-69) , F(<60)
marks = int(input("enter marks: "))
if (marks>=90):
    print("your grade is A")
elif (marks<=89) & (marks>=80):
    print("your grade is B")
elif(marks<=79) & (marks>=70):
    print("your grade is C")
elif(marks<=69) & (marks>=60):
    print("your grade is D")
else:
    print("your grade is F") 

## 8 take a character and check if it is a vowel or consonant.
char = input("enter a character: ")
vowels = ("a" , "e" , "i" , "o" , "u")
if char in vowels:  # we must need to use in to check does vowels in char or not.
    print("the character is vowel")
else:
    print("the character is consonant")
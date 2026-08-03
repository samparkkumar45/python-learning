## 1 take age and check if the person is a child (0-12), teenager (13-19) or adult (20+)
age = int(input("enter your age: "))
if (age>=0) & (age<=12):
    print("you are child")
elif (age>=13) & (age<=19):
    print("you are teenager")
else:
    print("you are adult")

## 2 take marks of 3 subjects and print grade: A if total >=90, B if total >=75, C if total>=50 , else fail.
sub1 = int(input("enter your marks of sub1:"))
sub2 = int(input("enter your marks of sub2:"))
sub3 = int(input("enter your marks of sub3:"))
total = sub1 + sub2 + sub3
if (total>=90):
    print("your grade will be: A")
elif (total>=75):
    print("your grade will be: B")
elif (total>=50):
    print("your grade will be: C")
else:
    print("you are fail")

## 3 take a number and check: if it is positive -> check if even or odd, if it is negative -> print negative number, if it is zero -> print zero
num = int(input("enter a number: "))
if (num>0):
    if (num % 2 == 0):
        print("the number is positive and even")
    else:
        print("the number is positive and odd")
if (num<0):
    print("the number is negative")
if (num==0):
    print("the number is zero")

## 4 take username and password from user and check if they are correct(use nested if).
username = input("enter username: ")
password = int(input("enter password: "))
if (username == "hello"):
    if(password == 342):
        print("unlock")
else:
    print("wrong username or password")

## 5 take year and check if it is a leap year or not.
year = int(input("enter a year:"))
if (year % 4 == 0):
    print("the year ia a leap year")
else:
    print("the year is not a leep year")
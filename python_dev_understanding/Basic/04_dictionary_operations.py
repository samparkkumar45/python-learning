student = {
    'Name' : 'sampark',
    'Age' : 25,
    'Courses' : ['Math' , 'Emglish' , 'Arts']
}
student['phone'] = '6567657'
student['Name'] = 'sam' # it update the value
print(student)
print(student['Name']) # to get specific string.
print(student['Phone']) # it return key error.
print(student.get('Phone')) # if key in not then it return none.
student.update({'Name' : 'Sam', # for update we can also use update method.
                'Age' : '23',
                'Phone' : '465'
                })
print(student)
del student['Age'] # it wil remove the value.
print(student)
age = student.pop('Age') # it also remove the value and also return the removed value.
print(age)
print(len(student)) # len give us the length of dict.
print(student.keys()) # Give all keys which is present in dict. 
print(student.values()) # only give value of the keys.
print(student.items()) # it return key and value in pair.
for key , value in student.items(): # it also return keys.
    print(key , value)
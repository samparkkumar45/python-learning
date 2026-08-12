# object Identity : is
language = 'python'
if language == 'python':
    print('True')
elif language == 'Java':
    print('language is java')
else:
    print('False')
# And where all must be true.
# or one must be true
# not convert true in flase
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
user = 'Admin'
logged_in = False
if not logged_in:
    print('Please log in')
else:
    print('Welcome')
a = [2,3,4]
b = [2,3,4]
print(id(a))
print(id(b))
print(a is b) # it check id
a = [2,3,4]
b = a  # here the id of both will be same.
print(id(a))
print(id(b))
print(a is b) 

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '' , () , [].
# Any empty mapping. For example, {}.

condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
condition = []
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

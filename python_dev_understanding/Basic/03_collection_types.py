#List
courses = ['Math' , 'Python' , 'English']
courses_2 = ['Arts' , 'Education']
num = [6,3,4,5,8]
print(len(courses))
print(courses[2]) # Indexing
print(courses[-1]) # negtive indexing
print(courses[5]) # index error
print(courses[0:2]) # here first index in included and second index is excluded.
courses.append('Art') # To add new somthing in list.
print(courses)
courses.insert(1 , 'Arts') # for add somethings at specific index we use insert function with indexing.
print(courses)
courses.insert(0 , courses_2) # it also add two list in each other.
print(courses)
courses.extend(courses_2) # best way to add second list into first list and extend only take one argument.
print(courses)
courses.remove('Math') # use it to remove specific value from the list.
print(courses)
courses.pop() # it remove the last value of the list . It is more useful when we use list in stack.
print(courses)
popped = courses.pop() # it will return the value which is poped.
print(popped)
courses.reverse() # it will revrese our list.
print(courses)
courses.sort() # it help us to arrange our list.
print(courses)
num.sort(reverse=True) # it give value in descending order.
print(num)
# we also use sorted function to sort our list.
print(min(num)) # it give the min value of our list.
print(max(num)) # it give max value of our list.
print(sum(num)) # it sum the all values of our list.
print(courses.index('Math')) # it give the index number of the value.
print('Art' in courses) # it check the value is in the list or not.
for  item in courses: # it give all values of our list.
    print(item)
for index , iteam in enumerate(courses): # it give the value of list with indexing.
   print(index , iteam)
for index , iteam in enumerate(courses , start=1): # it start indexing from 1 not from 0.
   print(index , iteam)
courses_str = ','.join(courses) # it give the value of our list in form of string.
print(courses_str)
new_list = courses_str.split(',') # It return back to the list.
print(new_list)
#Tuple # we can't modify it like list.
#Mutable
list_1 = ['math' , 'English']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 'Arts' # in list we can change the value.
print(list_1)
print(list_2) 
#Inmutable
tuple_1 = ('math' , 'English')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
tuple_1[0] = 'Arts'
print(tuple_1)
print(tuple_2)

#Sets # it is unordered.
my_set = {'Math' , 'History' , 'Arts'}
my_set_2 = {'Math' , 'History'}
print(my_set)
my_sets_3 = {'Math' , 'History' , 'Arts' , 'Math' ,  'Arts'} # sets not allow same value.
print(my_sets_3)
print('Math' in my_set) # we can do same thing with list and tuple but set is more optamize for this.
print(my_set.intersection(my_set_2)) # it help to check which value are same in sets.
print(my_set.difference(my_set_2)) # it give which values are not same in two or more sets. 
print(my_set.union(my_set_2)) # it combine the values of two list.

#Empty Lists
empty_list = []
empty_list = list()

#Empty tuple
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets 
empty_set = {} # This isn't right! It's a dict
empty_set = set()

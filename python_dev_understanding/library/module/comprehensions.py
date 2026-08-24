
nums = [1,2,3,4,5,6,7,8,9,10]
# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)
my_list = [n for n in nums]
print(my_list)
# I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)
my_list = [n*n for n in nums]
print(my_list)
# Using a map + lamdba
my_list = list(map(lambda n : n*n , nums))
print(my_list)
# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if (n % 2 == 0):
        my_list.append(n)
print(my_list)
# using a filter + lambda
my_list = list(filter(lambda n: n%2 !=0, nums))
print(my_list)
# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)
my_list = [(letter , num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Dictionary Comprehension
names = ['Bro' , 'Sampark' , 'Bee']
heros = ['Batman' , 'Superman', 'Spiderman']
print(list(zip(names , heros)))
# I wnat a dict{'name' : 'heros'} for each name,heros in zip(names, heros)
my_dict = {}
for name,heror in (zip(names,heros)):
    my_dict[name] = heror
print(my_dict)
my_dict = {name : hero for name , hero in zip(names,heros) if name != 'Bro'}
print(my_dict)

#Set Comprehesions
nums = [1,1,2,3,2,3,4,4,4,4,6,3,5]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)
my_set = {n for n in nums}
print(my_set)
#Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,1,2,3,2,4,4,5,6,3,5,6]
def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)

for i in my_gen:
    print (i)

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

my_list = map(lambda n:n*n,nums)
for i in my_list:
    print(i,end=", ")


#
my_list = []
for n in nums:
    if n%2==0:
        my_list.append(n)
print(my_list)

my_list = [n for n in my_list if n%2 == 0]
print(my_list)

my_list = filter(lambda n: n%2==0 ,nums)
print()

for i in my_list:
    print(i,end=", ")


#

my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)

names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']

for i in zip(names,heros):
    print(i,end=", ")

#
my_dict = {}
for name,hero in zip(names,heros):
    my_dict[name] = hero
print(my_dict)

my_dict = {name:hero for name,hero in zip(names,heros) if name != 'Peter'}
print(my_dict)

#
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = {n for n in nums}
print(my_set)

# Generator Expression

nums = [1,2,3,4,5,6,7,8,9,10]
def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)

my_gen = (n*n for n in nums)  ## generartor -> ()

for i in my_gen:
    print(i,end=" ")


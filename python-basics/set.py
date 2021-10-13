# A set is a collection which is both unordered and unindexed.


my_set = {'apple','banana','cherry'}
print(my_set)

# check whether the value exists or not
print('cherry' in my_set ) # True

#calculating the length of the set
print (len(my_set)) # 3


#converting se to the list
set_list = list(my_set)
print(set_list)  # ['apple', 'banana', 'cherry']

# set returns only the unique values  i.e removes duplicates
my_nums = {1,2,3,4,5,5}
print(my_nums) # {1, 2, 3, 4, 5}


# adding value to the set

#can only add the unique values i.e cannot add the values that already exists in set
my_nums.add(2)
my_nums.add(100)
print(my_nums)  # {1, 2, 3, 4, 5, 100}


# remove  the duplicates in a list 

my_list = [1,2,3,4,4,5]
new_list = set(my_list)
print(new_list) # {1, 2, 3, 4, 5}



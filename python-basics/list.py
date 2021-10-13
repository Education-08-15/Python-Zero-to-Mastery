# just like array list are the  ordered collection of items
list_1 = [1,2,3,4]
list_2 = ['a','b','c']
list_3 = [1,2,'a',True,{}]


#list slicing
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits[ : ]) # ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits[3:5]) # ['orange', 'kiwi']

print(fruits[0:6:2]) # ['apple', 'cherry', 'kiwi']

#------------------------------------------------------------------------------

#Changing list items i.e list are mutable
fruits[1] = 'stawberry'
print(fruits) # ['apple', 'stawberry', 'cherry', 'orange', 'kiwi', 'melon', 'mango']


#changing a range of values in list
numbers_list = [1,2,3,4,5,6,7,8]
numbers_list[0:3]= ['one','two','three']
print(numbers_list)


# calculating the length of the list
basket = [1,2,3,4,5,6]
print(len(basket)) #6

#append()	Adds an element at the end of the list
basket.append(200)
print(basket) #[1, 2, 3, 4, 5, 6, 200]

# insert Adds an element at the specified position
(basket.insert(3,33))
print(basket) #[1, 2, 3, 33, 4, 5, 6, 200]

# clear()	Removes all the elements from the list
clear_list = [1,2,3,4]
clear_list.clear()
print(clear_list) #[]

#removing

#pop removes the last element of the list
nums = [2,3,4,5,6]
nums.pop()
print(nums) # [2, 3, 4, 5]

# removes the element at 2nd index
nums.pop(2) 
print(nums) #[2,3,5]

#remove takes the value we wanna remove and removes it
values = ['one','two','three','four']
values.remove('three')
print(values) # ['one', 'two', 'four']
 


#sort  Sorts the list either number or string

sorting_num = [3,5,0,2,40,9,7]
sorting_num.sort()
print(sorting_num) #[0, 2, 3, 5, 7, 9, 40]


sort_string = ['a','f','p','n','w','q','c']
sort_string.sort()
print(sort_string)  # ['a', 'c', 'f', 'n', 'p', 'q', 'w']

#count()	Returns the number of elements with the specified value

count_value = [2,3,5,6,7,3,2,0,7]
print(count_value.count(2)) #2


#copy()	Returns a copy of the list
copied = count_value.copy()
print(copied) # [2, 3, 5, 6, 7, 3, 2, 0, 7]


#reverse()	Reverses the order of the list

data = [1,2,3,4]
data.reverse()
print(data) #[4,3,2,1]

# also provides reverse
list4 = [1,2,3,4,5,6]
print(list4[::-1])  # [6, 5, 4, 3, 2, 1]

#range
print(list(range(1,10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


#join

sentence = "!"
new_sentence = sentence.join(['hi','its','me','cxya'])
print(new_sentence) # hi!its!me!cxya

#list unpacking

a,b,c,* other,d = [1,2,3,4,5,6]

print(a) #1
print(b) #2
print(c) #3
print(other) #[4,5]
print(d) # 6



my_list = [
  {
    'a' :[1,2,3],
    'b' : 'hello',
    'c' : True
  },
  {
    'a' :[4,5,6],
    'b' : 'hi',
    'c' : True
  }
]

print(my_list [1]['a'][2]) #6
#Tuple 
# are like list but cannot be modified 
# immultable list

my_tuple = (1,2,3,4,5)

# calculating the length of the tuple
print (len(my_tuple )) # 5

#accessing the value at particular index
print(my_tuple[2]) # 3

#checking whether the value exists or not
print( 5 in my_tuple) # True

# new_tuple = my_tuple[1:3]
# print(new_tuple) #(2, 3)

new_tuple = my_tuple[1:2]
print(new_tuple) #(2,)  tuple with single value has comma at the end


x,y,z,* other= (1,2,3,4,6,7)

print(x) #1
print(y) #2
print(other) #[4,6,7]


# methods of tuples

my_tuples = (9,1,2,3,6,7,3,2,2)

# 1) Count
print(my_tuples.count(2))  # 3

# 2) index
print(my_tuples.index(6)) # 4


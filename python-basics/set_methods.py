# Methods in set

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# difference()
difference = my_set.difference(your_set)
print(difference) # {1,2,3}

#  discard()
# discard = my_set.discard(5)
# print(discard) # None
# print(my_set) # {1, 2, 3, 4}


#difference_update()
# my_set.difference_update(your_set)
# print(my_set) # {1,2,3}


#intersection()
intersect = my_set.intersection(your_set)
print(intersect) # {4, 5}

# isdisjoint() i.e nothing in common
isdisjoint = my_set.isdisjoint(your_set)
print(isdisjoint) # False

# issubset()
issubset = my_set.issubset(your_set)
print(issubset)  # False

# is superset()
superset = your_set.issuperset(my_set)
print(superset) #False

#union()
union = my_set.union(your_set)
print(union) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
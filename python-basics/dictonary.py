
#Dictonary (objects) an unordered key value pair


dictonary = {
  'a' : 1,
  'b' : 2
}

print(dictonary['b'])  #2

dictonary1 = {
  'a' :[1,2,3],
  'b' : {
    's':3
  } ,
  'c' : True
}

print (dictonary1)
print (dictonary1['b'])
print(dictonary1['a'][1]) # 2


# dictonary keys need to be immutable
# dictonary keys need to be unique otherwise it overwrites   
# can be given default value if doesnot exists

user = { 
  'name' : 'Shikshya',
  'age' : 22
}

print (user.get('interset')) #None


print(user.get('interest',['coding','eating','sleeping'])) #['coding', 'eating', 'sleeping']
print(user.get('age',19)) #22  uses the value that is given if not only takes the default 
print(user)


# creating a key value pair

user2 = dict(name="ASD",age=22,coder=True)
print(user2)  # {'name': 'ASD', 'age': 22, 'coder': True}


#Methos in dictonaries
# 1) Check if the key exists or not
print ('age' in user)  #True
print('lname' in user) #False

# check the keys exists or not
print('age' in user.keys()) #True

# check whether the values exists or not
 
print ('hello' in user.values()) #False
print ('Shikshya' in user.values()) #True

# grab all the items of the dictonary
print (user.items())  # dict_items([('name', 'Shikshya'), ('age', 22)])

# 2) clear()	Removes all the elements from the dictionary

user3 = {
  "name" : "abfbhjs"
}

print (user3.clear()) #None
print(user3) # {}

# 3) copy()	Returns a copy of the dictionary [NOte : after copying if we remove the dictonary from where value was taken it doesnot affects the copied user]

user4 = user.copy()
print(user4) # {'name': 'Shikshya', 'age': 22}

# 4) pop()	Removes the element with the specified key

user5 = {
  'a':2,
  'b':3,
  'c':4
}

user5.pop('a')
print(user5) # {'b': 3, 'c': 4}

# 5) popitem()	Removes the last inserted key-value pair

user6 = {
  'a':2,
  'b':3,
  'c':4
}
user6.popitem()
print(user6) # {'a': 2, 'b': 3}

# 6) update()	Updates the dictionary with the specified key-value pairs
user7 = {
  'a':2,
  'b':3,
  'c':4
}

user7.update({'b' :5})
print(user7) # {'a': 2, 'b': 5, 'c': 4}
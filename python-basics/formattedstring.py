# formatted strings

#  Before python 3 
print('Hi {0} you are {age} year old'.format("Shikshya", age =23))
print('Hi {0} you are {1} year old'.format("Shikshya", 23))
print('Hi {} you are {} year old'.format("Shikshya",23))
print('Hi {name} you are {age} year old'.format(name = "Shikshya", age =23))


# after python 3
name = "Shikshya"
age = 23
# print('Hi ' + name + ' you are ' + age + 'year old')  #error 
print (f'Hi {name} you are {age} year old')


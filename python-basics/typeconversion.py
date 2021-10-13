a = 100
print(type(a)) # interger

#converting integer into string
print(type(str(a))) # string

# converted into string and then again into integer and then checking the type 
print (type(int(str(a)))) # integer


# example

birth_year = input('what year were you born?')
current_year = 2021

current_age = current_year-int(birth_year)
print(current_age)
 
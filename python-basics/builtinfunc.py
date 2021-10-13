name = "Shikshya"

# 1) length  returns the length of the string
print(len(name))  #8

# 2) absolute  returns the positive value / modulus
print (abs(-2.7)) # 2.7
print (abs(-2.000)) #2.0

# 3) all Return True if all elements of the iterable are true (or if the iterable is empty)

all_true_values = [2>0, 3<5, 0==0]
print(all(all_true_values)) #true
print(all([2>0, 3>5, 0==0])) # false 
print(all([])) #True

#4)any Return True if any element of the iterable is true. If the iterable is empty, return False

print(any([2>0, 3>5, 0==0])) # true
print(any([])) #false

# 5) binary converts an integer number to a binary string prefixed with “0b”.

print(bin(10)) # 0b1010
print(bin(-3)) #-0b11

# 6) format function formats a specified value into a specified format.

# we can also use format to convert int in to binary
print(format(10 , "#b")) #0b1010
print(format(10 , "b")) #1010

# we can also use format to convert int in to hexadecimal
print (format(11,  "#x")) #0xb (lowercase)
print (format(11,  "#X")) #0XB (uppercase)

#  returns an error 'str' object cannot be interpreted as an integer
# print(bin('aa'))

# 6) bool Returns the boolean value of the specified object either true or false :: returns true unless the value os [],{},(),0,none,false
print(bool(5)) #true
print(bool(0)) #false
print(bool(1)) #true
print(bool()) #false
print(bool({})) #false
print(bool('True')) #true


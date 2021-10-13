print(2+4) # 6
print(2-4) #-2
print(2*4) #8
print(4/2) #2
print(2**3) #8

print(14//4) #3 i.e 4 times 3 is nearer to 14 

print(53%6) #5

# int ,float data types

print(type(2)) #int
print(type(2.34)) #float
print(type(2.0)) #float

print(type(2.9+1.1)) #float
print(type(4.4/ 2.2)) #float


#  built in math functions
print(round(3.1))  #3

print(abs(-20))  #20 i.e abs (abosulte value) means no negative number

print(pow(2,3)) # 2*2*2 = 8

 # complex data type
print(bin(2))  # 0b10  represents the binary number in python

print(bin ( 2+3)) # 0b101

num = int('0b101', 2)
print(num)  # 5 

print(int('0b1011101', 2)) #93

# does not supports memory management
x = 5
y = x
z = x
print(y)
print(z)
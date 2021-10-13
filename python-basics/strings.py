# string => something written inside ' ', "  "

string = "Hello World"
print(string)   

# string concatenation

print ('hello ' + 'cxya')

# ----------------------------------------------------------------

# indexing on string

indexes = "hello what's up ?"

#1) index[]
print(indexes[9]) # t
print(indexes[0]) # h
print(indexes[5]) # space
print(indexes[-1]) #?

# ----------------------------

#2) [start: stop]
print(indexes[1:7]) #ello w

#starts at given point and ends at end 
print(indexes[1:])  # ello what's up ?

#by default start is at 0
print(indexes[:5])  # hello

# by default starts at 0 and goes till the end
print(indexes[ : ])  # hello what's up ?

print(indexes[0: -1]) # hello what's up 

# -----------------------------------------------

#3) [start:stop:stepover]
print(indexes[3:8:2]) # l h

#provides the reverse
print(indexes [::-1])  # ? pu s'tahw olleh
print """
working with python lists now
"""


list = ['a','b','c']

print list

print list[0]

# same as list[0]
print list[:1][0] 

# repeat the list five times over
print list*(3+2)

# append first item to last of the list
print list + list[:1]

print list + list[2:]

print "Shallow copy of list " 
print list[:]

print "Insert a list at its own beginning"
list[:0] = list
print list

print "Iteratively Clear a list, removing the first item from the list each time"
copy  = list[:]
# this is true as long as copy is not empty
while copy:
	copy[:1]=[]
	print copy
	print " length = %s" % len(copy)

print "Iteratively Clear a list, removing the last item from the list each time"
copy  = list[:]
while copy:
	copy[-1:]=[]
	print copy
	print " length = ", len(copy)



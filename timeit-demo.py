# How to import a module (this could also be run from terminal as python -m timeout ...)
import timeit

# How to write a block of string inside the triple quotes, cool
print """
learning more operations on lists
"""

# Define a couple of functions we will use later and also import in a timeit call
# use list as stack
def printlist(mylist):
    print ':'.join (str(w) for w in mylist)
# square of a number
def sqr(x): return x*x;


# Start main body of code
# Change this value to increase the length of the range list you are working with
num = 5
# numbers from 1 to num
mylist = list(range(num))
# square of those numbers
#mylist = map(sqr, numbers)

#avg = int(sum(mylist)/float(len(mylist)))

# mid point index to split our list in half and manipulate/move the halves
halfpoint = len(mylist)/2

# Algo 1 : each time an element is found larger than halfpoint, move it to position 0
# effectively move the second half to the front in reversed form
# Uses for in, remove and insert methods for a list
def method1(mylist): 
	"""Method 1 using for in loop"""
	# square of those numbers
	#print "called"
	for w in mylist[:]:
		if w>halfpoint:
			mylist.remove(w)
			mylist.insert(0, w)
	#printlist(mylist)
	#print mylist

#method1();


# Algo 2: use methods in list element without using iterations
def method2(mylist):
	"""Method2 using list methods"""
	# Take the latter half
	stufftomove=mylist[halfpoint:]
	# reverse it
	stufftomove.reverse()
	# remove the second half from list
	mylist[halfpoint:]=[]
	# put it back in the front
	mylist[:0]=stufftomove
	#printlist(mylist)
	#print mylist

# Now is the fun part

# Run each algo and calculate time to profile them using timeit
# I got this on my machine
# 0.690565814377
# [0, 1, 2, 3, 4]
# 0.0256983344071
# [0, 1, 2, 3, 4]
# [Finished in 0.8s]
#


print timeit.timeit("method1(mylist)", setup="from __main__ import method1; mylist = list(range(50))", number=10000)
print mylist

# square of those numbers
print timeit.timeit("method2(mylist)", setup="from __main__ import method2; mylist = list(range(50))", number=10000)
print mylist

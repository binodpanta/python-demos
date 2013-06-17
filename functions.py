"""Exploring function behavior in Python"""

"""
This will do what?
"""

# In the version shown in comments below, the default value empty for L is only evaluated o nce
# So for calls beyond the first one, L is already set!
"""
def f(a, L=[]):
    L.append(a)
    return L
"""

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)


"""
Try using named formal parameters,
"""

def poly(name,*coeffs,**coeffs2):
	"""Polynomial function"""
	print "\nEquation name is ", name
	if (coeffs):
		print "Coeffs are ", (','.join (str(a) for a in coeffs))

	if (coeffs2):
		skeys = sorted(coeffs2.keys())
		print "Named Coeffs are", (','.join ( (kw+"="+str(coeffs2[kw])) for kw in skeys) )


# this works fine
poly("sin(x)")

# now pass some  coeffs
poly("sin(x)", 1,4,5)


# now pass some  coeffs
poly("sin(x)", 1,4,5, a=5,b=10,c=11)

"""
Try lambda functions 
"""

# This returns a function that represents a polynomial
# Input is a dictionary with a,b,c being required keys
def polyf(**coeffs):
	"""Returns a lambda functoin"""
	return lambda x: coeffs['a']*x*x + coeffs['b']*x+coeffs['c']

# now returns a lambda function that will evaluate 2nd order polynomial with coeffs a, b, c when called
f = polyf(a=1,b=2,c=3)


print "Help doc for this function = ", polyf.__doc__


print f(0.1)
print f(0)


# now returns a lambda function that will evaluate 2nd order polynomial with coeffs a, b, c when called
f2 = polyf(a=1,b=20,c=3)
print f2(0.1)
print f2(0)



"""
Showing that the value passed to a function is by object reference
Each time we call this it changes the value of the passed list
"""

def change(changeit):
	changeit[:0]=[changeit[0]-1]
	return changeit

l = [100]
print "Starting value of list"
print l
for i in range(15):
	change(l)

print "After a few calls of a Funtion, list should have changed"
print l
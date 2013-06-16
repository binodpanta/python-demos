print "Python indices practice, weird circulars and other fun!\n"

print """
Here is how the indexes can be visualized for Python lists
Negative indices work too!
 +---+---+---+---+---+
 | H | e | l | p | A |
 +---+---+---+---+---+
 0   1   2   3   4   5
-5  -4  -3  -2  -1
"""

word = "awordwithafewletters"

# simple access zero based
print word[1]
print word[0]

# Using negative indices to get the last three letters
print "Here are the last three letters\
 of the word " + word[-3:]
 
# positive index to get the first three letters
print "Here are the first three letters\
 of the word " + word[:3]

# indices are circular in python!

import unicodedata

print "Python indices practice, weird circular\n"

print """
 +---+---+---+---+---+
 | H | e | l | p | A |
 +---+---+---+---+---+
 0   1   2   3   4   5
-5  -4  -3  -2  -1
"""

word = "awordwithafewletters"

print word[1]

print word[0]

print "Here are the last three letters\
 of the word " + word[-3:]


print "Here are the first three letters\
 of the word " + word[:3]


print """
Now playing with unicode
"""

print """
Let's try some Japanese!
"""

ucode = u"aUnicode[\u3020]string with unicode [\u3070] characters".encode('utf-8')
print ucode


print """
Let's try some Chinese!
"""

ucode = u"aUnicode[\u5400] string with unicode [\u9F00] characters".encode('utf-8')
print ucode

print "Using unicodedata library for some fun"

print unicodedata.bidirectional(u'\u4E00')

print u'\u6789'.encode('utf-8')





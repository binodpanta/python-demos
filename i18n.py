# indices are circular in python!

import unicodedata



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





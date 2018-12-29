from functools import *


s = ["h" , "hey" , "hell" , "hello" , "Namaste"]


def LongWord(s):

    return reduce(lambda a,b  : a if len(a)>len(b) else b , s )

print(LongWord(s))









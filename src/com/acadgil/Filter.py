

def MyFilter(func, seq):

    for i in seq:
        if func(i) == True:
            yield (i)


def Even(s):
    if s % 2 == 0:
        return True

L = [2,3,4,5,6,7,8]

r =list( MyFilter(Even, L))

print(r)
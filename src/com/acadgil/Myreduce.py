def do_sum(a,b):

    return a+b

def my_reduce(func, seq):

    sum = 0

    for i in range(len(seq)):
        sum = sum+i

    return sum

k = my_reduce(do_sum , [2,3,4,5,6,7,8])


print(k)
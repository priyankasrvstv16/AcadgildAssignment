
def Myreduce(fnc, seq):

	t = seq[0]

	for next in seq[1:]:

		t = fnc(t, next)

	return t

r = Myreduce((lambda x,y: x*y),[3,1,5,1,3,2])

print(r)
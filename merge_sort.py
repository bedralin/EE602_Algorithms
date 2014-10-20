import math

def merge(A,p,q,r):
    p = int(p)
    q = int(q)
    r = int(r) 
    n1 = int(q - p+1 )
    n2 = int(r - q)
    print n1
    L = range(0,n1+1)
    R = range(0,n2+1)
    for i in range(0,n1):
	L[i] = A[p+i-1]
    for j in range(0,n2):
	R[j] = A[q+j]
    L[n1] = float('inf')
    R[n2] = float('inf')
    i=0	
    j=0
    for k in range(p,r):
	if L[i] <= R[j]:
	    A[k] = L[i]
	    i = i+1
	elif A[k] == R[j]:
	    j = j+1


def merge_sort(A,p,r):
    if p < r:
	q = int(math.floor((p+r)/2))
	merge_sort(A,p,q)
	merge_sort(A,q+1,r)
	merge(A,p,q,r)

A = [4,3,7,1,8,10]

p = 0
r = len(A)-1
print "A was:",A
merge_sort(A,p,r)
print "A is:",A


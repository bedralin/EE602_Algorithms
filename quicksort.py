
count = 0;
def partition(A,p,r):
    global count
    x = A[r]
    i = p -1  
    for j in range(p,r):
	if A[j] <= x:
	    i = i + 1
	    A[i],A[j] = A[j],A[i]
	count+=1
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def quicksort(A,p,r):
    global count
    count+=1
    if p < r: 
	q = partition(A,p,r)
	quicksort(A,p,q-1)
	quicksort(A,q+1,r)

A=[3,1,6,9,2,4]
A=[1,2,3,4,5,6]
p = 0 
r=len(A)-1
print "A was:",A
quicksort(A,p,r)
print "A is:",A
print "count is:",count	    


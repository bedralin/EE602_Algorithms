
def sequential_search(A,n):
    for j in range(0,n):
	print j
	if sequential_search(A,j) != 0:
	    print j	
	    return j
	
A = [0,3,4,7,9,2]
n = len(A)
j = sequential_search(A,n)
print "j is:",j

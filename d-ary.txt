#!/usr/bin/env python

"""
Bronson Edralin
EE602 Algorithms
HW #2
Problem 6-2

d-ary heap
"""

# MACROS
def PARENT(i,d):
    return int((i - 1) / d)
def CHILD(i,c,d):
    return int(3 * i + c + 1)
def MIN():
    return int(-2147483648)

# DATA, have to create DATA object
class Heap:
    def __init__(self, elements, d, heap_size, length):
        self.elements = elements
	self.d = d
	self.heap_size = heap_size
	self.length = length

    @property
    def elements(self):
        return self.elements
    @elements.setter
    def elements(self, element):
        self.elements.append(element)

    @property
    def d(self):
        return self.d
    @d.setter 
    def d(self,d):
	self.d = d

    @property
    def heap_size(self):
        return self.heap_size
    @heap_size.setter
    def heap_size(self, heap_size):
	self.heap_size = heap_size

    @property
    def length(self):
        return self.length
    @length.setter
    def length(self, length):
	self.length = length


def max_heapify(heap, int(i)):
    largest = i
    for k in range(0, heap.d):
	child = CHILD(i, k, heap.d)
	if (child < heap.heap_size) and (heap.elements[child] > heap.elements[largest]):
	    largest = child
    if (largest != i):
	# Swapping
	tmp = heap.elements[i]
	heap.elements[i] = heap.elements[largest]
	heap.elements[largest] = tmp

	max_heapify(heap, largest)


def extract_max(heap):
    max = heap.elements[0]
    heap.elements[0] = heap.elements[heap.heap_size - 1]
    heap.heap_size -= 1
    max_heapify(heap, 0)
    return max


def increase_key(heap, i, key):
    if (key < heap.elements[i]):
        print "Error: new key smaller than current key\n")
	sys.exit()  

    while (i > 0) and (heap.elements[PARENT(i,heap.d)] < key):
        heap.elements[i] = heap.elements[PARENT(i,heap.d)]
        i = PARENT(i,heap.d)
    
    heap.elements[i] = key

def insert(heap, key):
    heap.heap_size += 1
    heap.elements[heap.heap_size - 1] = MIN()
    increase_key(heap, heap.heap_size - 1, key)


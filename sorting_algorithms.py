import random

#-------------SELECTION SORT----------------
def selection_sort(stuff):
    size = len(stuff)
    for i in range(size):
        for j in range(i+1,size):
            if stuff[j] < stuff[i]:
                stuff[j] ^= stuff[i]
                stuff[i] ^= stuff[j]
                stuff[j] ^= stuff[i]

    print(stuff) 

#-------------BUBBLE SORT----------------
def bubble_sort(stuff):
    size = len(stuff)
    for i in range(size):
        for j in range(size-i-1):
            if stuff[j] > stuff[j+1]:
                stuff[j] ^= stuff[j+1] 
                stuff[j+1] ^= stuff[j] 
                stuff[j] ^= stuff[j+1]
    print(stuff) 
            
#-------------MERGE SORT----------------
def merge(stuff,left,right,start):
    current = start
    l = r = 0
    left_size = len(left)
    right_size = len(right)

    while l < left_size and r < right_size:
        if left[l] <= right[r]:
            stuff[current] = left[l]
            l += 1
            current += 1
        else:
            stuff[current] = right[r]
            r += 1
            current += 1

    while l < left_size:
        stuff[current] = left[l]
        l += 1
        current += 1

    while r < right_size:
        stuff[current] = right[r]
        r += 1
        current += 1

    return stuff    

def merge_sort(stuff,start,end):
    if start >= end:
        return stuff
    
    mid = (end+start)//2

    left = merge_sort(stuff[start:mid+1],start,mid)
    right = merge_sort(stuff[mid+1:end+1],mid+1,end)
    return merge(stuff,left,right,start)

#-------------QUICK SORT----------------
def partition(stuff,start,end):
    pivot = random.randint(start,end)
    partitioner = start  
    
    if pivot != end:
        stuff[pivot] ^= stuff[end]
        stuff[end] ^= stuff[pivot]
        stuff[pivot] ^= stuff[end]
    
    for i in range(start,end):
        if stuff[i] < stuff[end]:
            stuff[i] ^= stuff[partitioner]
            stuff[partitioner] ^= stuff[i]
            stuff[i] ^= stuff[partitioner]
            partitioner += 1
    
    stuff[partitioner] ^= stuff[end]
    stuff[end] ^= stuff[partitioner]
    stuff[partitioner] ^= stuff[end]

    return partitioner

def quick_sort(stuff,start,end):
    if start < end:
        pi = partition(stuff,start,end)
        quick_sort(stuff,start,pi)
        quick_sort(stuff,pi+1,end)
    

stuff = [1,40,9,6,7,0,0,3,-900,190]
selection_sort(stuff) 
bubble_sort(stuff)
sorted_list = merge_sort(stuff,0,len(stuff)-1)
print(sorted_list)
stuff = [1,40,9,6,7,0,0,3,-900,190]
quick_sort(stuff,0,len(stuff)-1)
print(stuff)

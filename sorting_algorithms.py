#-------------SELECTION SORT----------------
def selection_sort(stuff):
    size = len(stuff)
    for i in range(size):
        for j in range(i+1,size):
            if stuff[j] < stuff[i]:
                temp = stuff[j]
                stuff[j] = stuff[i]
                stuff[i] = temp

    print(stuff) 

#-------------BUBBLE SORT----------------
def bubble_sort(stuff):
    size = len(stuff)
    for i in range(size):
        for j in range(size-i-1):
            if stuff[j] > stuff[j+1]:
                temp = stuff[j]
                stuff[j] = stuff[j+1] 
                stuff[j+1] = temp 

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
    partitioner = start-1  

    if pivot != end:
        temp = stuff[end]
        stuff[end] = stuff[pivot]
        stuff[pivot] = temp
    
    for i in range(start,end):
        if stuff[i] <= stuff[end]:
            partitioner += 1 
            if stuff[i] != stuff[partitioner]:   
                temp  = stuff[partitioner]
                stuff[partitioner] = stuff[i]
                stuff[i] = stuff[partitioner]

    if stuff[end] != stuff[partitioner+1]:
        temp = stuff[end]
        stuff[end] = stuff[partitioner+1]
        stuff[partitioner+1] = temp
            
    return partitioner+1

def quick_sort(stuff,start,end):
    if start < end:
        pi = partition(stuff,start,end)
        quick_sort(stuff,start,pi-1)
        quick_sort(stuff,pi+1,end)
        
"""
stuff = [[1],[40],[9],[6],[7],[0],[0],[3],[-900],[190]]
selection_sort(stuff) 
bubble_sort(stuff)
sorted_list = merge_sort(stuff,0,len(stuff)-1)
print(sorted_list)
quick_sort(stuff,0,len(stuff)-1)
print(stuff)"""

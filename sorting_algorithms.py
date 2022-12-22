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
def merge(left,right,start):
     
    
    
def merge_sort(stuff,start,end):
    if start >= end:
        return stuff
    
    mid = (end+start)//2

    left = merge_sort(stuff[start:mid],start,mid)
    right = merge_sort(stuff[mid+1:end],mid+1,end)
    return merge(stuff,left,right,start)
    

def quick_sort(stuff):
    pass


stuff = [1,40,9,6,7,0,0,3,-900,190]
selection_sort(stuff) 
bubble_sort(stuff)
sorted_list = merge_sort(stuff)

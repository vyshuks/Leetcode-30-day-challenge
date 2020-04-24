
def find_pivot(arr, start, end):
    if end < start:
        return -1
    if start == end:
        return start
    
    mid = (end+start) // 2

    if mid < end and arr[mid] > arr[mid+1]:
        return mid
    if mid > start and arr[mid] < arr[mid-1]:
        return mid-1
    
    if (arr[start] >= arr[mid]):
        return find_pivot(arr, start, mid-1); 
      
    return find_pivot(arr, mid + 1, end); 

    
    
    return find_pivot(arr, mid, end)

def binary_search(arr, start, end, target):
    if end < start:
        return -1 
    mid = (end+start) // 2
    
    if arr[mid] == target:return mid 

    if target > arr[mid]:
        return binary_search(arr, mid+1, end, target)
    
    else:
        return binary_search(arr, start, mid-1, target)

    
    

def search(arr, target):
    start = 0
    end = len(arr)
    pivot = find_pivot(arr, start, end-1)
    print(pivot)
    if pivot == -1:
        return binary_search(arr,0,end-1,target)
    if arr[pivot] == target:return pivot
    if target >= arr[0]:
        print("ttt")
        return binary_search(arr, 0, pivot-1, target)
    else:
        return binary_search(arr, pivot+1, end-1, target)

arr = [1,3,5]
end = len(arr)
print(search(arr, 1))
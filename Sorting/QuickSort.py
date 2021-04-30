def find_pivot(arr,first,last):
    p = arr[first]
    left = first+1
    right = last
    while True:
        while(left<=right and p>=arr[left]):
            left+=1
        while(left<=right and p<=arr[right]):
            right-=1
        if(right<left):
            break
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[first],arr[right] = arr[right],arr[first]
    return right

def quickSort(arr,first,last):
    if(first<last):
        pr = find_pivot(arr,first,last)
        quickSort(arr,first,pr-1)
        quickSort(arr,pr+1,last)

arr = [1,9,2,10,3,11,89,53]
quickSort(arr,0,len(arr)-1)
print(arr)
            

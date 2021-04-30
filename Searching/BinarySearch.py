def binarySearch(arr,T):
    arr.sort()
    left = 0
    ans= 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if(arr[mid]==T):
            ans = mid
            break
        elif(arr[mid]>T):
            right = mid-1
        else:
            left = mid+1
    return ans
arr = [1,4,8,9,10,23,2,3]
T = 3
print(binarySearch(arr,T))
            
            

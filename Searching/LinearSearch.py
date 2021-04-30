def LinearSearch(arr,T):
    for i in range(len(arr)):
        if(arr[i] == T):
            return i
arr = [1,2,5,12,4,33]
print(LinearSearch(arr,4))

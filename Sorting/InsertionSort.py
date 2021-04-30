def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
arr = [10,9,2,3,15,4,1,100,200,400,300]
insertionSort(arr)
print(arr)


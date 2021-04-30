def selectionSort(arr):
    for i in range(len(arr)):
        minpos = i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[minpos]):
                minpos = j
        arr[i],arr[minpos] = arr[minpos],arr[i]

arr = [10,2,3,4,1,188,199]
selectionSort(arr)
print(arr)

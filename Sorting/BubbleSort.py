def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i],arr[j] = arr[j],arr[i]
   

arr = [1,45,3,2,90]
BubbleSort(arr)
print(arr)

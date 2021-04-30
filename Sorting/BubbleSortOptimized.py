import datetime as dt
def BubbleSort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i],arr[j] = arr[j],arr[i]
                swapped = True
        if not swapped:
            break
   
bg = dt.datetime.now()
arr = [1,2,4,5,6,7,8,9]
BubbleSort(arr)


print(arr)
print(dt.datetime.now()-bg)

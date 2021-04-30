def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left_list = arr[:mid]
        right_list = arr[mid:]
        mergeSort(left_list)
        mergeSort(right_list)
        i,j,k = 0,0,0
        while(i<len(left_list) and j<len(right_list)):
            if(left_list[i]<right_list[j]):
                arr[k] = left_list[i]
                k+=1
                i+=1
            else:
                arr[k] = right_list[j]
                k+=1
                j+=1
        while(i<len(left_list)):
            arr[k] = left_list[i]
            i+=1
            k+=1
        while(j<len(right_list)):
            arr[k] = right_list[j]
            j+=1
            k+=1
arr = [10,3,4,2,1,9,12,45]
mergeSort(arr)
print(arr)
        
            
        
        

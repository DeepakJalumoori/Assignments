'''Given two sorted arrays, merge them to get another sorted array
Example Input:
5     #size of first array
2 4 11 17 91      #first array
 
 4       #size of second array
 3 7 9 100 #second array
Example Output :
2 3 4 7 9 11 17 91 100
'''



def merge_sort(arr1, arr2):
    m, n = len(arr1), len(arr2)
    arr3 = [0] * (m + n)
    
    i, j, k = 0, 0, 0
    
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1
    
    while i < m:
        arr3[k] = arr1[i]
        k += 1
        i += 1
    
    while j < n:
        arr3[k] = arr2[j]
        k += 1
        j += 1
    
    for i in range(m):
        arr1[i] = arr3[i]
    
    for i in range(m, m + n):
        arr2[i - m] = arr3[i]

if _name_== "_main_":
    m = int(input())
    arr1 = list(map(int, input().split()))
    
    n = int(input())
    arr2 = list(map(int, input().split()))
    
    merge_sort(arr1, arr2)
    
    print(" ".join(map(str, arr1)))
    print(" ".join(map(str, arr2)))
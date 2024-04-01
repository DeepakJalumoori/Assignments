'''Given an empty list and a stream of N numbers. Print min, max, sum, average and 
mode (optional and if there are multiple modes then print any) after insertion of each 
element from the stream to the list.
Example Input:
5
2 4 3 2 -3
Example output
▪ min, max, sum, average and mode after addition of 2 is 2, 2, 2, 2, 2.
▪ min, max, sum, average and mode after addition of 4 is 2, 4, 6, 3, 4.
▪ min, max, sum, average and mode after addition of 3 is 2, 4, 9, 3, 4.
▪ min, max, sum, average and mode after addition of 2 is 2, 4, 11, 2.75, 2.
▪ min, max, sum, average and mode after addition of -3 is -3, 3, 8, 1.6, 2.
'''

N = int(input())
arr = list(map(int, input().split()))
sums = 0
for i in arr:
    sums += i

minimum = arr[0]
for j in arr:
    if j < minimum:
        minimum = j

if minimum == arr[0]:
    maximum = arr[1]
    for w in arr:
        if w > maximum:
            maximum = w
else:
    maximum = arr[0]
    for w in arr:
        if w > maximum:
            maximum = w

average = sums / len(arr)
print(sums)
print(minimum)
print(maximum)
print(average)


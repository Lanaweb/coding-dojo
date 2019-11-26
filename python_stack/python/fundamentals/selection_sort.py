
arr = [8,4,5,7,6,3,2,1,0,9]

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        min = arr[i]
        for j in range(0+i,len(arr)):
            if min > arr[j]:
                min = arr[j]
                minIndex = j
                print("the min is", min)
                print("the minTemp is", minIndex)
        print("the i is", i)
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        print(arr[i],arr[j])
        print(arr)
    return arr

print(selectionSort(arr))


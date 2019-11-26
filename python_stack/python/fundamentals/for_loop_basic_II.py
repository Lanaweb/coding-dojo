def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] >0:
            arr[i] = "big"
    return arr
    
print(biggie_size([-1, 3, 5, -5]))

def count_positives(arr):
    countpos = 0
    for val in arr:
        if val >0:
            countpos += 1
    arr.append(countpos)
    return arr

print(count_positives([-1,1,1,1]))
    
def sum_total(arr):
    sum = 0
    for val in arr:
        sum += val
    return sum
print(sum_total([1,2,3,4]) )
    
print(sum_total([6,3,-2]))

def length(arr):
    count = 0
    for val in arr:
        count += 1
    return count

print(length([37,2,1,-9]))
##print(minimum([37,2,1,-9]))

def minimum(arr):
    if len(arr) <1:
        return False
    min = arr[0]
    for val in arr:
        if min > val:
            min = val
    return min

print(minimum([37,2,1,-9]))
print(minimum([]))

def maximum(arr):
    if len(arr) < 1:
        return False
    max = arr[0]
    for val in arr:
        if max < val:
            max = val
    return max

print(maximum([37,2,1,-9]))
print(maximum([]))


def ultimate_analysis(arr):
    if len(arr) < 1:
        return False
    sum = 0
    ave = 0
    min = arr[0]
    max = arr[0]
    length = len(arr)
    for val in arr:
        if min > val:
            min = val
        if max < val:
            max = val
        sum += val
    ave = sum/len(arr)
    return {'sumTotal': sum, 'average': ave, 'minimum': min, 'maximum': max, 'length': length}

print(ultimate_analysis([37,2,1,-9]))


def reverse_list(arr):
    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr

print(reverse_list([37,2,1,-9]))

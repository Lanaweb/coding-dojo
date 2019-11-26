def countdown(num):
    new = []
    for i in range(num, -1, -1):
        new.append(i)
    return new
        
def print_and_return(arr):
    print(arr[0])
    return(arr[1])

print_and_return([1,2])

def first_plus_length(arr):
    sum = 0;
    sum = arr[0] + len(arr)
    return sum

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(arr):
    new = []
    if len(arr) < 2:
        return False
    for i in range(len(arr)):
        if arr[i] > arr[1]:
            new.append(arr[i])
    return new

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))
    
def length_and_value(size, value):
    arr = []
    for i in range(size):
        arr.append(value)
    return arr
print(length_and_value(4,7))
print(length_and_value(6,2))

# --PRACTICE--


def binary_search(array,element):
    start = 0;
    end = len(array) - 1;
    while(start <= end):
        middle_index = (start + end) // 2
        if(array[middle_index] == element):
            return array[middle_index]
        if(array[middle_index] > element):
            end = middle_index - 1
        else:
            start = middle_index + 1
    return array[start]

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
array = sorted(array)
element = int(input("Enter an element to get ceiling: "))
print(binary_search(array,element))

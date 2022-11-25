# --PRACTICE--

# If the input array is sorted and don't know whether it is ascending or descending we can use the below code

def order_agnostic_binary_Search(array,element):
    start = 0;
    end = len(array) - 1;
    while(start <= end):
        middle_index = (start + end) // 2

        if(array[middle_index] == element):
            return True

        if(array[0] < array[len(array)-1]):
            if(array[middle_index] > element):
                end = middle_index - 1
            else:
                start = middle_index + 1
        else:
            if(array[middle_index] < element):
                end = middle_index - 1
            else:
                start = middle_index + 1
    return False

# For Demo purpose
size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
array = sorted(array,reverse=True)
element = int(input("Enter an element to search: "))
print(order_agnostic_binary_Search(array,element))

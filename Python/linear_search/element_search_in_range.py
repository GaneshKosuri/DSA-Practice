# Implementing Searching of an element in a given range
# Return true if found else return false

def find_element(array,element,start_index,end_index):
    array_length = len(array)
    if (start_index < 0 or end_index >= array_length):
        return False
    for i in range(start_index,end_index+1):
        if(element == array[i]):
            return True
    return False

size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
search_element = int(input("Enter the number to search: "))
[start_index,end_index] = list(map(int,input("Enter range separated with space : ").strip().split()))[:2]
print(find_element(array,search_element,start_index,end_index))
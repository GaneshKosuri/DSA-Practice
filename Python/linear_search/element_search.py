# Implementing Searching of an element
# Return true if found else return false

def find_element(array,element):
    for i in range(0,len(array)):
        if(element == array[i]):
            return True
    return False

size = int(input("Enter Array Size : "))
array = list(map(int,input("Enter the numbers separated by space : ").strip().split()))[:size]
search_element = int(input("Enter the number to search: "))
print(find_element(array,search_element))
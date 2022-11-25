# --PRACTICE--
# IF we are having an array with infinite length

def binary_search(array,element,start,end):
    while(start <= end):
        middle_index = (start + end) // 2
        if(array[middle_index] == element):
            return True
        if(array[middle_index] > element):
            end = middle_index - 1
        else:
            start = middle_index + 1
    return False

def main_answer(array,element):
    start = 0
    end = 1

    while(element > array[end]):
        temp = end + 1
        end = end + (end - start + 1) * 2
        start = temp

    return binary_search


main_answer([1,1,1,1,1,1],3)
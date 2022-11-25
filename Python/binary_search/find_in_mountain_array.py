# --HARD--
# https://leetcode.com/problems/find-in-mountain-array/description/


# Solution starts
def find_peak_element_index(self,mountain_arr: 'MountainArray') -> int:
    start = 0
    end = mountain_arr.length() -1
    while(start < end):
        middle_index = start + (end - start)//2
        if(mountain_arr.get(middle_index) > mountain_arr.get(middle_index + 1)):
            end = middle_index
        else:
            start = middle_index + 1
    return start

def search_element(self,target: int, mountain_arr: 'MountainArray',start: int,end: int,isAsc: bool) -> int:
    while(start <= end):
        middle_index = start + (end - start)//2
        value = mountain_arr.get(middle_index)
        if(value == target):
            return middle_index
        if(isAsc):
            if(value > target):
                end = middle_index - 1
            else:
                start = middle_index + 1
        else:
            if(value < target):
                end = middle_index - 1
            else:
                start = middle_index + 1
    return -1


def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
    end_index = self.find_peak_element_index(mountain_arr)
    first_trail = self.search_element(target,mountain_arr,0,end_index,True)
    if(first_trail != -1):
        return first_trail
    else:
        last_index = mountain_arr.length() - 1
        return self.search_element(target,mountain_arr,end_index+1,last_index,False)

# Solution ends
#find out which two numbers  gives a  sum 9 and return thrie index, list is always sorted

def find_sum(li, target):
    left_ptr = li[0]
    right_ptr= len(li)-1

    while left_ptr< right_ptr:
        curSum = li[left_ptr]+li[right_ptr]
        if curSum < target:
            #increment left ptr
            left_ptr+=1
        elif curSum > target:
            #decrease right ptr with one position
            right_ptr -= 1
        else:
            return [left_ptr,right_ptr]

    return []




print(find_sum(li=[1,3,4,5,7,10,11], target=9))


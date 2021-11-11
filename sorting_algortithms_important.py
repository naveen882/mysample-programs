#Quick sort:
"""
Choose any randomn element in the below case we always choose the last element as pivot element and then insert the elements lesser thn oivot in left ist and greater or equal to in the right list
so recursivley this gets sorted

the best time for this is nlogn 
and the worst time is n^^2
"""
 
def quick_sort(li):
    if len(li)<=1:
        return li
    else:
        pivot = li.pop()

    items_greater= []
    items_lesser = []

    for i in li:
        if i < pivot:
            items_lesser.append(i)
        else:
            items_greater.append(i)

    return  quick_sort(items_lesser) + [pivot] + quick_sort(items_greater)


print(quick_sort([0,9,3,82,7,5]))


#Insertion Sort

"""
This takes two elements ata time compare the left element and if it is greater than the right element it swaps the element, it does that until unless the left element is lesser
the best time for this is n
and the worst time is n^^2
"""

def insertion_sort(li):

	if len(li)<=1:
		return li
	else:
		indexing_length= range(1,len(li))
		for i in indexing_length:
			key = li[i]
			while li[i-1]> key and i>=0:
				li[i-1],li[i]= li[i],li[i-1]
				i = i-1
		return li

print(insertion_sort([0,9,3,82,7,5]))

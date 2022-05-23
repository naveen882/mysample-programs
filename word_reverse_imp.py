s= "This is a boy. Boy like cricket."

l= s.split(" ")

print(l)
print("length of list {}".format(len(l)))

left = 0
right= len(l)-1

while left < right:
    left_flag = False
    right_flag = False

    if "." in l[left]:
        l[left] = l[left][:-1]
        left_flag = True

    if "." in l[right]:
        l[right] = l[right][:-1]
        right_flag = True

    l[left], l[right] = l[right], l[left]
    if left_flag:
        l[left] = l[left] + '.'
    if right_flag:
        l[right] = l[right] + '.'
    left += 1
    right -= 1


print(" ".join(l)) 

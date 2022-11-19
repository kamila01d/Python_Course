def odwracanie(L, left, right):
    limit = (right - left)//2

    if (right-left) % 2 != 0:
        limit +=1

    j = 0
    for i in range(left,(limit+left)):
        val = L[i]
        L[i] = L[right-j]
        L[right-j] = val
        j += 1
    return L

def recursiveOdwracanie(L, left, right):
    if(left<right):
        tmp = L[left]
        L[left] = L[right]
        L[right] = tmp
        recursiveOdwracanie(L,left+1,right-1)
    return L


L = [0,1,2,3,4,5,6,7,8,9,10]

print(recursiveOdwracanie(L,1,2))
print(odwracanie([0,1,2,3,4,5,6,7,8,9,10],9,10))
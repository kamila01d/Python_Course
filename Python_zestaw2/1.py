list1 = [1, 2, [3, 4, [5, 6], 5], 3, [4, 5]]

def get_max_depth(lst,l,max_=0):

    for i in range(len(lst)):
        max_ = max(max_, l)

        if type(lst[i]) == list:
            max_ = get_max_depth(lst[i], l+1, max_)
            l -= 1
    return max_


def increment_nested(lst, l, max_depth):

    for i in range(len(lst)):

        if type(lst[i]) == list:
            if l == max_depth - 1:
                lst[i].append(lst[i][-1] + 1)
                return lst

            increment_nested(lst[i], l+1, max_depth)
            l -= 1
    return lst

def append_incremented(lst):


    max_depth = get_max_depth(lst, 0)
    if max_depth == 0:
        lst.append(lst[-1]+1)
        return lst
    l = increment_nested(lst, 0, max_depth)
    return (l)

print(append_incremented(list1))






def remove_all(lst, value):
    i = 0
    while i < len(lst):
        if lst[i] == value:
            temp = lst[i]
            lst[i] = lst[len(lst) - 1]
            lst[len(lst)-1] = temp
            lst.pop()            
        else:
            i += 1
    return lst


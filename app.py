def binary_search(item,my_list):
    found=False
    first=0
    last=len(my_list)-1
    while first <=last and found==False:
        midpoint=(first+last)//2
        if my_list[midpoint]==item:
            found=True
        else:
            if my_list[midpoint]<item:
                first=midpoint+1
            else:
                last=midpoint-1
    return found

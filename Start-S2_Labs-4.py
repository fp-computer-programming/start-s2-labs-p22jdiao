# Author: JD 01/26/2022

def double_every_other(lst):
    for i,v in enumerate(lst):
        if i%2 != 0:
            lst[i] *= 2
            
    return lst
    pass
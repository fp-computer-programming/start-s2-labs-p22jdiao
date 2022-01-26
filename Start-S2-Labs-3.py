# Author: JD 01/26/2022

def comes_after(st, l): 
    lst = []

    for i,v in enumerate(st):
        try:
            if v.upper() == l or v.lower() == l:
                if st[i+1].isalpha() == True:
                    lst.append(st[i+1])
        except IndexError:
            lst.append("")
            

    lst = "".join(lst)

    return lst
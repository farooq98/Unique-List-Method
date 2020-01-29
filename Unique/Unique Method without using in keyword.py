def Unique(lst):
    try:
        temp = [lst[0]]
        a = False
        for i in lst:
            a = True
            for j in temp:
                if j == i:
                    a = False
                    break
            if a:
                temp.append(i)
        return temp
    except:
        return "list is empty"

x = [1,2,2,6,3,4,5,4,3,5,6,1,9]
print(Unique(x))

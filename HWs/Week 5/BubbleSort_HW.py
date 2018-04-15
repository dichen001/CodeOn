ls = [2,3,6,100,1,70,50,60]

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                print(alist[i], ">", alist[i+1])
                # temp = alist[i]
                # alist[i] = alist[i+1]
                # alist[i+1] = temp
                alist[i], alist[i+1] = alist[i+1], alist[i]

bubbleSort(ls)
print(ls)
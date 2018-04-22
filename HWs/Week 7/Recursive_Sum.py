ls = [1,2,3,4,5]

def SolveSum(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        return ls[0] + SolveSum(ls[1:])


print SolveSum(ls)
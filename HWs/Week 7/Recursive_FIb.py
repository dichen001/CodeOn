
def solveFib(val):
    if val == 0 or val == 1:
        return val
    else:
        return solveFib(val-1) + solveFib(val-2)

print solveFib(0)
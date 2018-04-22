
def solveFact(val):
    if val == 0 or val == 1:
        return 1
    else:
        return val * solveFact(val - 1)

print solveFact(3)
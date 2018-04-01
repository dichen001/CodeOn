ls = [2,3,6,100,1,70,50,60]

for last in range(len(ls)-1, -1, -1):
    print ls

    # Index
    temp_large = 0
    for i in range(last + 1):
        if ls[i] > ls[temp_large]:
            temp_large = i
    ls[last], ls[temp_large] = ls[temp_large], ls[last]
    print ls

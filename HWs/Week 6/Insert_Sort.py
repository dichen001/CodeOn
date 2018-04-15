#Insertion Sort

ls = [16,2,1,10,20]

for i in range(1, len(ls)):
    temp = ls[i]
    curr_indx = i
    while curr_indx>0 and ls[curr_indx-1] > temp:
        ls[curr_indx] = ls[curr_indx-1]
        curr_indx -= 1
    ls[curr_indx] = temp
print ls
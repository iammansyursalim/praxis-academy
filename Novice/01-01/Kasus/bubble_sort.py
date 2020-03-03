def bubblesort(list):
    i = 0
    for j in range (len(list)-1):
        for i in range (len(list)-1-j):
            if list[i]>list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
        i+=1
        print(i, list)
    
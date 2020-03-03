def selectionsort(list):
    i = 0
    for i in range(len(list)-1):
        awal = i
        for j in range(i+1,len(list)):
            if list[j] < list[awal]:
                awal = j
        i+=1
        list[awal],list[i]=list[i], list[awal]
        print(i, list)
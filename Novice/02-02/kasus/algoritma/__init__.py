def bubblesort(list):
    i = 0
    for j in range (len(list)-1):
        for i in range (len(list)-1-j):
            if list[i]>list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
        i+=1
        print(i, list)

def insertionsort(list):
    for j in range(len(list)-1,-1,-1):
        nilai = list[j]
        kosong = j
        while kosong <(len(list)-1) and list[kosong+1]>list[kosong]:
            list[kosong] = list[kosong+1]
            kosong = kosong+1
            list[kosong] = nilai
        print(list)

def mergesort(list):
    print('Memecah List', list)
    n = len(list)
    if n < 2:
        return list
    else:
        mid=n//2
        left=list[:mid]
        right=list[mid:]

        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i < len (left) and j < len (right):
            if left[i]>right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
            k=k+1
        while i < len (left):
            list[k]=left[i]
            i=i+1
            k=k+1
        while j < len (right):
            list[k]=right[j]
            j=j+1
            k=k+1
    print('Menggabungkan List', list)

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

def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2
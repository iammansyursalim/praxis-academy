def quicksort(list,awal,akhir):
    if awal < akhir:
        pindex = partisi(list,awal,akhir)
        quicksort(list,awal,pindex-1)
        quicksort(list,pindex+1,akhir)

def partisi(list,awal,akhir):
    tengah = int(akhir/2)
    pivot = list[tengah]
    pindex = awal
    for i in range(awal,tengah):
        if list[i]>=pivot:
            list[i],list[pindex]=list[pindex],list[i]
            pindex = pindex + 1
    list[pindex],list[tengah]=list[tengah],list[pindex]
    print(list)
    return pindex

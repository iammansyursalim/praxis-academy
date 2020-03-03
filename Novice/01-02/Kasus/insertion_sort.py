def insertionsort(list):
    for j in range(len(list)-1,-1,-1):
        nilai = list[j]
        kosong = j
        while kosong <(len(list)-1) and list[kosong+1]>list[kosong]:
            list[kosong] = list[kosong+1]
            kosong = kosong+1
            list[kosong] = nilai
        print(list)
import bubble_sort
import insertion_sort
import merge_sort
import shell_sort
import selection_sort

list_bs = [2,4,7,9,11,44,35]
print('Data Sebelum : ', list_bs)
print('Bubble Sort : ')
bubble_sort.bubblesort(list_bs)

print('=====================================================')

list_is = [76,33,46,64,20]
print('Data Sebelum : ', list_is)
print('Insertion Sort : ')
insertion_sort.insertionsort(list_is)

print('=====================================================')

list_ms = [2,5,60,43]
print('Data Sebelum : ', list_ms)
print('Merge Sort : ')
merge_sort.mergesort(list_ms)

print('=====================================================')

list_ss=[11,57,33,44,55,81]
print('Data Sebelum : ', list_ss)
print('Selection Sort : ')
selection_sort.selectionsort(list_ss)

print('=====================================================')
list_shs = [12, 34, 54, 2, 3]
n = len(list_shs) 
print ("Data Sebelum : ") 
for i in range(n): 
    print(list_shs[i]), 

shell_sort.shellSort(list_shs) 
  
print ("\nShell Sort : ") 
for i in range(n): 
    print(list_shs[i])


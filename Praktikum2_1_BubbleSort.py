# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:00:55 2024

@author: faiz
"""

def bubble_sort(arr):
    n = len(arr)            #ngitung panjang array 

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def main():
    print("Nama : Faiz FIrdaus PRiyanto")  #Nama
    print("Nim  :0640023000005")
    print("Bubble Sort ")
    input_user = input("Masukkan angka dipisahkan oleh koma: ")   #Input user 
    angka = []
    for x in input_user.split(","):
        angka.append(int(x))
   
    #menampilkan list sebelum urut
    print("Angka yang belum diurutkan:")
    print(angka) 

    bubble_sort(angka)
    
    #menampilkan list setelah urut 
    print("List setelah diurutkan:")
    print(angka)  

    
if __name__ == "__main__":  #program utama
    main()
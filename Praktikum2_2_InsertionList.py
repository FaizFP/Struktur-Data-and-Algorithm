# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:59:50 2024

@author: faiz
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    print("Nama : Faiz FIrdaus PRiyanto")  #Nama
    print("Nim  :0640023000005")
    print("InsertionSort ")

    
    #input user 
    angka = input("Masukkan Angka dipisahkan oleh koma: ")
    list_angka = []  # angka angka yang dinput user 
    for x in angka.split(","):
        list_angka.append(int(x))  # Menggunakan list_angka untuk menghindari konflik nama variabel

    
    # Menampilkan list sebelum diurutkan
    print("List sebelum diurutkan:")
    print(list_angka)

    # Mengurutkan list menggunakan insertion sort
    insertion_sort(list_angka)

    # Menampilkan list setelah diurutkan
    print("List setelah diurutkan:")
    print(list_angka)

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:02:16 2024

@author: faiz
"""

#Faiz Firdaus Priyanto
#064002300005
#Informatika
#Program yang dapat menjumlahkan dua buah vektor dengan menerapkan class dan object

class Vector:
    def __init__(self):    #inisialisasi 
        self.nama = "Nama : Faiz Firdaus Priyanto"
        self.nim =  "NIM  : 064002300005"
        self.prak = "Prak 3 - Elkom 2 "
        self.angka1 = 2
        self.angka2 = 10
        self.angka3 = 5
        self.angka4 = -2
        
    def tor(self,angka1,angka2,angka3,angka4):   #logic 
        return angka1 + angka3 , angka2 + angka4
    
    
    
    
def main():
    oVector = Vector()  
    
    hasil = oVector.tor(oVector.angka1, oVector.angka2 , oVector.angka3 , oVector.angka4)  #pemangillan fungsi 
    #Tampilan buat user    
    print(oVector.nama)
    print(oVector.nim)
    print(oVector.prak)
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    print("Vector 1 :" , oVector.angka1 , "," ,oVector.angka2)  #pemanggilan fungsi 
    print("Vector 2 :" , oVector.angka3 , "," , oVector.angka4)
    print("Hasil Penjumlahan dari vector 1 dan 2 :", hasil)   #hasil 
    
    
    
    
    
if __name__ == '__main__':
    main()      
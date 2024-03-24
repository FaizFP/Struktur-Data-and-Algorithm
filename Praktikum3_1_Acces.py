# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:36:59 2024

@author: faiz
"""
#Faiz Firdaus Priyanto
#064002300005



class Employee:
    total = 0
    
    
    
    def __init__(self):
        #identitas 
        self.nama = "Nama : Faiz Firdaus Priyanto"
        self.nim =  "NIM  : 064002300005"
        self.prak = "Prak 3 - Elkom 1 "
        
    def pegawai(self, name, salary):
        self.name = name
        self.salary = salary 
        Employee.total += 1 #total ketika objek Employee dibuat
        
    def tampilan(self):
        print("Name:", self.name, ", Salary:", self.salary)  #untuk menampilkan nama dan gaji pegawai
        
   

def main():
    # Membuat beberapa objek Employee
    oEmployee = Employee()
    pekerja1 = Employee()
    pekerja1.pegawai("boy", "20000")
    pekerja2 = Employee()
    pekerja2.pegawai("foujin", "50000")
   
    
    # Menampilkan informasi pegawai dan total pegawai
    print(oEmployee.nama)
    print(oEmployee.nim)
    print(oEmployee.prak)
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    
    
    pekerja1.tampilan()

    pekerja2.tampilan()
    
    print("Total Employee:",Employee.total)
    
if __name__ == '__main__':
    main()
    

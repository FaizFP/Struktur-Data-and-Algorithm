#Faiz Firdaus Priyanto
#064002300005
#Informatika
import random

class List:
    def __init__(self):
        self.tampil_1 = "====[Latihan1]==== "
        self.list_name1 = "List"
        self.main_list = []
        self.tampil_2 = "====[Latihan2]==== "
        self.list_name2 = "List"
        self.tampil_3 = "====[Latihan3]==== "
        self.list_name3 = "List"
        self.list_tambahan = []

    
    def lat_1(self, ukuran_list):           
        # Menambahkan angka secara otomatis menggunakan metode append
        for _ in range(ukuran_list):  
            i = random.randint(0, 10)
            self.main_list.append(i)
        
    def tampilan_lat1(self):    # Menampilkan list utama
        print(self.tampil_1)  
        print(self.list_name1,"1" , self.main_list)
   
    def lat_2(self, angka, index):    # Menambahkan angka ke dalam list menggunakan metode insert
        self.main_list.insert(index, angka)

    def tampilan_lat2(self):    # Menampilkan list utama
        print(self.tampil_2)  
        print(self.list_name2,"1", self.main_list)
    
    def lat_3(self):    # Menambahkan angka ke dalam list menggunakan metode extend
        for _ in range(5):  
            b = random.randint(0, 10)
            self.list_tambahan.append(b)
        self.main_list.extend(self.list_tambahan)

    def tampilan_lat3(self):
        print(self.tampil_3)
        print(self.list_name3,"2", self.list_tambahan)

    def tampilan_gabungan(self):
        print("====[Latihan3]====")
        print("List1 dan List 2 yang sudah digabungkan", self.main_list)
    
    def lat_4(self):
        hasil_jumlah = sum(self.main_list)
        print("====[Latihan4]====")

        #Penjumlahan
        print("1. Penjumlahan isi dalam list ")
        print("Hasil Penjumlahan :", hasil_jumlah)

        #mencari angka 
        check_number = int(input("2. Mencari angka yang double : "))
        count_check_number = self.main_list.count(check_number)
        if count_check_number > 1:
            print("Angka", check_number, "muncul : ", count_check_number,)
        else:
            print("Angka", check_number, "hanya muncul 1 kali dalam list.")

        #Menghitung sebuah panjang dari list 
        print("3.Menghitung panjang list ")
        cari_panjang = len(self.main_list)
        print("Panjang List : ",cari_panjang)

        #Mencari index dari list
        print("4.Mencari index ")
        input_angka = int(input("Angka yang dicari : ")) 
        index_input = self.main_list.index(input_angka)
        print(f"Indeks dari elemen {input_angka} adalah:", index_input)

    def lat_5(self):
        print("====[Latihan5]====")
        #pop /dikeluarkan 
        pops = int(input("Masukkan Elemen yang mau dipop : "))
        pop = self.main_list.pop(pops)
        print("UPDATED LIST : ", self.main_list)
        
        #del/menghapus
        del self.main_list[4]  #menghilangkan index 4 
        print("Updated list setelah operasi del ",self.main_list)

        #remove
        angka_hapus = int(input("masukkan angka yang akan dihapus : "))
        self.main_list.remove(angka_hapus) #input agar sesuai dengan apa yang mau dihapus 
        print("UPDATED LIST SETELAH REMOVE ", self.main_list)





       

def main():
    Olist_1 = List()

    # Input ukuran list
    ukuran_list = int(input("Masukkan ukuran list: "))

    Olist_1.lat_1(ukuran_list)
    Olist_1.tampilan_lat1()

    # Latihan 2
    
    index = 0  # menambahkan indeks dari 0
    angka_tambahan = int(input("NIM : "))
    Olist_1.lat_2(angka_tambahan, index)
    Olist_1.tampilan_lat2()  # 

    # Latihan 3
    Olist_1.lat_3()
    Olist_1.tampilan_lat3()
    Olist_1.tampilan_gabungan()
    
    #Latihan 4 
    Olist_1.lat_4()
    #Latihan 5 
    Olist_1.lat_5()
    
    
if __name__ == '__main__':
    main()



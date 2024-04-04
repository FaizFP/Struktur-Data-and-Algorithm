#Faiz Firdaus Priyanto 
#064002300005
#Informatika


class Stack:
    def __init__(self):
        print("STACK OPERATION")
        print("1.PUSH")
        print("2.POP")
        print("3.TAMPILAN STACK")
        print("4.CLOSE")
        self.tack = []   #isi dalam list 


    def push(self):   #untuk push/append
        input_nama = str(input("Masukkan nama : "))
        self.tack.append(input_nama)

    def pop(self):  #pop/mengkeluarkan 
        angka_keluar = self.tack.pop()
        print("Pop:",angka_keluar)
    
    def tampilan_stack(self): #Tampilan ketika stack kosong 
        if len(self.tack) == 0:
            print("Stack kosong")
        else:
            print("Stack:")  #Jika ada stack 
            for item in (self.tack):
                print("[",item,"]")

    def stack_hasil(self):
        for item in (self.tack):
                print("[",item,"]")
    



def main():  #Program utama 
    OStack = Stack()
    while True: #perulangan 
        pilihan = str(input("Masukkan pilihan : "))
        if pilihan == "1":
            OStack.push()
        elif pilihan == "2":
            OStack.pop()
        elif pilihan == "3":
            OStack.tampilan_stack()
        elif pilihan == "4":
            OStack.stack_hasil()
            break       
         

if __name__ == '__main__':
    main()
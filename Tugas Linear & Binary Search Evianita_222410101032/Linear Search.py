print("Masukkan angka yang ingin dicari dari data di bawah ini!")

def sequential(database, cari):
     
     indek = len(database)
     value = False
     data1 = []

     for i in range (0,indek):
          if cari == database[i]:
               value = True
               data1.append(i)
     if value == True:
          print("data berhasil ditemukan! ")
     for i in data1:
          print("terletak pada indeks: ", i)
     if value == False:
          print("maaf, data yang dicari tidak tersedia")
     return

database = [4,7,3,2,1,5,6,8,9,0,7,7,8,8,9,9,11,13]
print("data: ", database)

cari = int(input("Inputkan data angka yang ingin anda cari: "))
sequential(database, cari)


import json
import os
from datetime import date
from itertools import combinations
import time

lises = []
line = []
data = dict ()

def cleanView():
    os.system('cls')

def back():
    print('\n')
    input("\t\t\t>>> Click enter to back <<<\t\t")
    menuUtama()

def dates():
    objek = date.today()
    hari = (str(objek.day),"-",str(objek,month),"-",str(objek.year))
    return (hari)

def header():
    print("-" * 70)
    print("NO\tTanggal\t\tNama\t\t\tBerat(kg)\tPrice")
    print("-" * 70)

def menuUtama():
    cleanView()
    print('''
                ---    MAIN MENU    ---   
    - - - - - - - - - - - - - - - - - - - - - - - -
    -  1. Add New Item                 --->       -
    -  2. Undelivered Item             --->       -
    -  3. Delivered Item               --->       -
    -  0. Exit                         --->       -
    - - - - - - - - - - - - - - - - - - - - - - - -
    - - -                                     - - -
                       - - - - -
    ''')

def readDone(filename,jenis):
    line.clear()
    with open(filename) as file:
        see = json.load(file)[jenis]
        for a in see:
            line.append(a)
        
        if (len(line)>0):
            no = 1
            print("-" * 70)
            print(jenis.center(70))
            print('-' * 70 + '\n')

            header()
            for i in line:
                if len(i['Nama Barang']) <- 70:
                        j - 20 - len(i['Nama Barang'])
                        print(
                        f"{no}"
                        f"\t{i['tanggal']}"
                        f"\t{i['Nama Barang'] + ' '*j}"
                        f"\t{i['Berat Barang']}"
                        f"\t\t{i['Nilai Barang']}"
                        )
                        no += 1
            print('-' * 70)

        else:
            print('-' * 70)
            print('Tidak Ada Barang Yang Berhasil Dikirim'.center(70))
            print('-' * 70)

def reader():
    with open('undelivered.json') as file :
        data = json.load(file)
    return data

def readerDone():
    with open('delivered.json') as file:
        data = json.load(file)
    return data

def additems():

    while True:
        cleanView()
        print('-' * 70)
        print('Tambahkan Barang'.center(70))
        print('-' * 70)
        confirm = input('\n Ingin Menambahakan Data? [y]/[n] \n')
        if confirm == 'y':
            item_name = input("Nama Barang : ")
            weight = input("Berat Barang : ")
            value = input("Nilai Barang: ")
            itemdata = {
                "Tanggal"       : dates(),
                "Nama Barang"   : item_name,
                "Berat Barang"  : weight,
                "Nilai Barang"  : value
            }
            lises = reader()["Data Barang Yang Belum Dikirim"]
            lises.append(itemdata)
            data = {
                "Data Barang yang Belum Dikirim" : lises
            }

            with open('undelivered.json', 'w') as file:
                json.dump(data,file,indent-4)
            
            print("Item Sukses Ditambahakan")
            time.sleep(2)
        elif confirm == 'n' :
            break

def knapsack(capacity):
    cleanView()
    data = []
    nama = []
    # global delivered
    # deliverec = []

    with open('undelivered.json') as file :
        see = json.load(file)["Data Barang Yang Belum Dikirim"]
        for a in see:
            data.append(a)
            nama.append(a['Nama Barang'])

    combname = []
    indeks = 1
    while indeks <- len(nama):
        coname = combinations(nama,indeks)
        for x in coname:
            combname.append(list(x))
            indeks+-1

    value = []
    # berat = []
    value_sementara = []
    berat_sementara = []
    ind = 0
    while ind < len(combname):
        for x in data:
            if x['Nama Barang'] in combaname[ind]:
                value_sementara.append(int(x['Nilai Barang']))
                berat_sementara.append(int(x['Nilai Barang']))
        value.append(([sum(value_sementara),sum(berat_sementara)] +  combname[ind]))
        del value_sementara[::]
        del berat_sementara[::]
        ind +- 1

    global fix
    


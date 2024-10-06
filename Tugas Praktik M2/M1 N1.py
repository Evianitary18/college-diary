import os
import csv

os.system("cls")

kamus = []
with open('kamus.csv') as csv_kamus :
    csv_reader = csv.reader(csv_kamus, delimiter = ',')
    for row in csv_reader:
        kamus.append([row[0],row[1]])

# print(kamus)

maxim1 = []
for i in range(len(kamus)):
    maxim1.append(len(kamus[i][0]))

maxim2 = []
for i in range(len(kamus)):
    maxim2.append(len(kamus[i][1]))

# BUBBLE SORT UNTUK BAHASA INGGRIS - BAHASA INDONESIA
def bubble_sort_inggris_indonesia(data, urutan_huruf):
    pj_data = len(data)
    for i in range(pj_data):
        for j in range(pj_data-i-1):
            kebenaran = "yes"
            if len(data[j][0]) <= urutan_huruf :
                pass
            elif len(data[j+1][0]) <= urutan_huruf :
                pass
            else:
                for x in range(urutan_huruf) :
                    if ord(data[j][0][x]) == ord(data[j+1][0][x]):
                        kebenaran = "yes"
                    else:
                        kebenaran = "no"
                        break
                if kebenaran == "yes":
                    if ord(data[j][0][urutan_huruf]) > ord(data[j+1][0][urutan_huruf]):
                        data[j], data[j+1] = data[j+1], data[j]
    
    if urutan_huruf <= max(maxim1):
        bubble_sort_inggris_indonesia(data, urutan_huruf+1)

# BUBBLE SORT BAHASA INDONESIA - BAHASA INGGRIS
def bubble_sort_indonesia_inggris(data, urutan_huruf):
    pj_data = len(data)
    for i in range(pj_data):
        for j in range(pj_data-i-1):
            kebenaran = "yes"
            if len(data[j][1]) <= urutan_huruf :
                pass
            elif len(data[j+1][1]) <= urutan_huruf :
                pass
            else:
                for x in range(urutan_huruf) :
                    if ord(data[j][1][x]) == ord(data[j+1][1][x]):
                        kebenaran = "yes"
                    else:
                        kebenaran = "no"
                        break
                if kebenaran == "yes":
                    if ord(data[j][1][urutan_huruf]) > ord(data[j+1][1][urutan_huruf]):
                        data[j], data[j+1] = data[j+1], data[j]
    
    if urutan_huruf <= max(maxim2):
        bubble_sort_indonesia_inggris(data, urutan_huruf+1)

# CARA MEMANGGIL INGGRIS-INDONESIA
bubble_sort_inggris_indonesia(kamus,0)
print("BUBBLE SORT INGGRIS - INDONESIA")
for i in kamus :
    print(f"{i[0]} : {i[1]}")

# CARA MEMANGGIL INDONESIA - INGGRIS
bubble_sort_indonesia_inggris(kamus,0)
print("BUBBLE SORT INDONESIA - INGGRIS")
for i in kamus :
    print(f"{i[1]} : {i[0]}")

# SELECTION SORT BAHASA INGGRIS - BAHASA INDONESIA
def selection_sort_inggris_indonesia(data,terkecil, idx, urutan_huruf) :
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if len(data[j][0]) <= urutan_huruf :
                pass
            elif len(data[i][0]) <= urutan_huruf :
                pass
            else :
                kebenaran = "yes"
                for y in range(urutan_huruf):
                    if ord(data[j][0][y]) == ord(data[i][0][y]) :
                        kebenaran = "yes"
                    else:
                        kebenaran = "no"
                        break
                if kebenaran == "yes":
                    if ord(data[j][0][urutan_huruf]) < ord(data[i][0][urutan_huruf]) :
                        if terkecil == 0 and idx == 0 :
                            terkecil = ord(data[j][0][urutan_huruf])
                            idx = j
                        elif terkecil == 0 and idx != 0 :
                            if ord(data[j][0][urutan_huruf] < terkecil) :
                                terkecil = ord(data[j][0][urutan_huruf])
                                idx = j
                        else:
                            if ord(data[j][0][urutan_huruf]) < terkecil :
                                terkecil = ord(data[j][0][urutan_huruf])
                                idx = j
        if idx != 0 :
            data[i], data[idx] = data[idx],data[i]
        terkecil = 0
        idx = 0

    if urutan_huruf <= max(maxim1) :
        selection_sort_inggris_indonesia(kamus, terkecil, idx, urutan_huruf+1)
# CARA MEMANGGIL SELECTION SORT BAHASA INGGRIS - BAHASA INDONESIA
selection_sort_inggris_indonesia(kamus, 0,0,0)
print("SELECTION SORT INGGRIS - INDONESIA")
for i in kamus:
    print(f"{i[0]} : {i[1]}") 

# SELECTION SORT BAHASA INDONESIA - BAHASA INGGRIS
def selection_sort_indonesia_inggris(data,terkecil, idx, urutan_huruf) :
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if len(data[j][1]) <= urutan_huruf :
                pass
            elif len(data[i][1]) <= urutan_huruf :
                pass
            else :
                kebenaran = "yes"
                for y in range(urutan_huruf):
                    if ord(data[j][1][y]) == ord(data[i][1][y]) :
                        kebenaran = "yes"
                    else:
                        kebenaran = "no"
                        break
                if kebenaran == "yes":
                    if ord(data[j][1][urutan_huruf]) < ord(data[i][1][urutan_huruf]) :
                        if terkecil == 1 and idx == 1 :
                            terkecil = ord(data[j][1][urutan_huruf])
                            idx = j
                        elif terkecil == 1 and idx != 1 :
                            if ord(data[j][1][urutan_huruf] < terkecil) :
                                terkecil = ord(data[j][1][urutan_huruf])
                                idx = j
                        else:
                            if ord(data[j][1][urutan_huruf]) < terkecil :
                                terkecil = ord(data[j][1][urutan_huruf])
                                idx = j
        if idx != 1 :
            data[i], data[idx] = data[idx],data[i]
        terkecil = 1
        idx = 1

    if urutan_huruf <= max(maxim2) :
        selection_sort_indonesia_inggris(kamus, terkecil, idx, urutan_huruf+1)

# CARA MEMANGGIL SELECTION SORT BAHASA INDONESIA - BAHASA INGGRIS
selection_sort_indonesia_inggris(kamus, 0,0,0)
print("SELECTION SORT INDONESIA - INGGRIS")
for i in kamus:
    print(f"{i[1]} : {i[0]}") 

# INSERTION SORT BAHASA INGGRIS - BAHASA INDONESIA
def insertion_sort_inggris_indonesia(data, urutan_huruf):
    for i in range (1, len(data)) :
        for j in range(i):
            if len(data[i][0]) <= urutan_huruf :
                pass
            elif len(data[i-1][0]) <= urutan_huruf :
                pass
            else :
                yorn = "yes"
                for y in range(urutan_huruf):
                    if ord(data[i][0][y]) == ord(data[i-1][0][y]) :
                        yorn = "yes"
                    else:
                        yorn = "no"
                        break
                if yorn == "yes":
                    if ord(data[i][0][urutan_huruf]) < ord(data[i-1][0][urutan_huruf]) :
                        data[i-1], data[i] = data[i], data[i-1]
                        i -= 1
    if urutan_huruf <= max(maxim1) :
        insertion_sort_inggris_indonesia(data, urutan_huruf+1)

# CARA MEMANGGIL INSERTION SORT BAHASA INGGRIS- BAHASA INDONESIA
insertion_sort_inggris_indonesia(kamus, 0)
print("INSERTION SORT BAHASA INGGRIS - BAHASA INDONESIA")
for i in kamus:
    print(f"{i[0]} :{i[1]}")

# INSERTION SORT BAHASA INDONESIA - BAHASA INGGRIS
def insertion_sort_indonesia_inggris(data, urutan_huruf):
    for i in range (1, len(data)) :
        for j in range(i):
            if len(data[i][1]) <= urutan_huruf :
                pass
            elif len(data[i-1][1]) <= urutan_huruf :
                pass
            else :
                yorn = "yes"
                for y in range(urutan_huruf):
                    if ord(data[i][1][y]) == ord(data[i-1][1][y]) :
                        yorn = "yes"
                    else:
                        yorn = "no"
                        break
                if yorn == "yes":
                    if ord(data[i][1][urutan_huruf]) < ord(data[i-1][1][urutan_huruf]) :
                        data[i-1], data[i] = data[i], data[i-1]
                        i -= 1
    if urutan_huruf <= max(maxim2) :
        insertion_sort_indonesia_inggris(data, urutan_huruf+1)

# CARA MEMANGGIL INSERTION SORT BAHASA INGGRIS- BAHASA INDONESIA
insertion_sort_indonesia_inggris(kamus, 0)
print("INSERTION SORT BAHASA INDONESIA - BAHASA INGGRIS")
for i in kamus:
    print(f"{i[1]} :{i[0]}")

# MENU PILIHAN USER

print("Pilihan Kamus : ")
print("(a) Kamus Bahasa Inggris - Bahasa Indonesia")
print("(b) Kamus Bahasa Indonesia - Bahasa Inggris")
pilih = input("Pilihan a/b: ")

print("")
print("Pilihan Algoritma : ")
print("(a) BUBBLE SORT")
print("(b) SELECTION SORT")
print("(c) INSERTION SORT")
pilih2 = input("Pilihan (a/b/c) : ")

if pilih == "a" :
    if pilih2 == "a" :
        bubble_sort_inggris_indonesia(kamus,0)
        print("BUBBLE SORT INGGRIS - INDONESIA")
        for i in kamus :
            print(f"{i[0]} : {i[1]}")
    elif pilih2 == "b" :
        selection_sort_inggris_indonesia(kamus, 0, 0, 0)
        print("SELECTION SORT INGGRIS - INDONESIA")
        for i in kamus :
            print(f"{i[0]} : {i[1]}")
    elif pilih2 == "c" :
        insertion_sort_inggris_indonesia(kamus, 0)
        print("INSERTION SORT INGGRIS - INDONESIA")
        for i in kamus :
            print(f"{i[0]} : {i[1]}")
    else :
        pass
elif pilih == "b" :
    if pilih2 == "a" :
        bubble_sort_indonesia_inggris(kamus,0)
        print("BUBBLE SORT INDONESIA - INGGRIS")
        for i in kamus :
            print(f"{i[1]} : {i[0]}")
    elif pilih2 == "b" :
        selection_sort_indonesia_inggris(kamus, 0, 0, 0)
        print("SELECTION SORT INDONESIA - INGGRIS")
        for i in kamus :
            print(f"{i[1]} : {i[0]}")
    elif pilih2 == "c" :
        insertion_sort_indonesia_inggris(kamus, 0)
        print("INSERTION SORT INDONESIA - INGGRIS")
        for i in kamus :
            print(f"{i[1]} : {i[0]}")
    else :
        pass
else :
    pass
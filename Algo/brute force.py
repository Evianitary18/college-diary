import random

# brute force metode cara dalam mencari solusi menggunakan kode dan mengandalkan pc kita
# sebuah solusi yang dipikirkan seorang programmer berapa kali. mengandalkan kecepatan spesifikasi komputer

# password = int(input("password: "))

# while True:
#     check = random.randint(0,999)
#     if check == password:
#         print(f"logged, {check}")
#         break
#     else:
#         pass

# SOAL LAB

# def Sequential_Search(dlist, item):

#     pos = 0
#     found = False  

#     while pos <len(dlist) and not found:
#         if dlist[pos] == item:
#             found = True
#         else:
#             pos = pos + 1

#     return found, pos

# print(Sequential_Search([3, 5, 12, 15, 21, 22, 34, 36], 21))

# password = input("password: ")
# data = "qwertyuiopasdfghjklzxcvbnm1234567890"
# data_list = list(data)
# check = ""

# while (check!=password)


# bil = [3,5,12,15,21,22,34,36]

# for i in bil:
#     if i == 21:
#         print(f"ada {i}")
#     else:
#         pass

# bil = [3,5,12,15,21,22,34,36]

# for i in range (len(bil)):
#     if bil[i] == 21:
#         print(i)
#     else:
#         pass
bil = [3,5,12,15,21,22,34,36]

def findId(menu_list, idx=0):
    if menu_list[idx] == 21:
        return idx
    else:
        return findId(menu_list, idx+1)
    
print(findId(([3,5,12,15,21,22,34,36])))

# mendeklarasikan findId yang menerima parameter array 
array = [3,5,12,15,21,22,34,36]
loop = 1
idx = 0

while idx < len(array):
    if array [idx] == 21:
        print(idx, loop)
        break
    else:
        idx += 1
        loop += 1



# def findId(menu_list, idx=0, loop = 0):
#     if menu_list[idx] == 21:
#         return idx, loop
#     else:
#         # loop += 1
#         return findId(menu_list, idx+1, loop +1)
    
# print(findId(([3,5,12,15,21,22,34,36])))

# BINARY SEARCH
# -----> Algovisualizer website-----> memvisualisasikan bagaimana algo bekerja

# Clue tugas lab 1 iterasi dari 1, melakukan looping dari 1 sampai inputan kita
# funct () melakukan perulangan for i in range 1,21
# dicek apaka 21 bisa dibagi i
    

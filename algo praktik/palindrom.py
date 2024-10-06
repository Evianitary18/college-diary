# Untuk mengambil data dengan slicing
data = ["ando", "rika", "dina"]

data2 = data[1]
print(data2)

# Mencari tau panjang data yang ada di list
data3 = len(data)
print(data3)

# Menambah data dalam list

data4 = "Jojo"
data.append(data4)
print(data)

# Menambah list dengan lis
data5 = ["oke", "oki"]
data.extend(data5)
print(data)

data[1] = "oke"
print(data)

# Cara menghapus data dengan remove
data.remove("ando")
print(data)

# Menghapus data paling belakang
data.pop()
print(data)

# join mengubah dari list menjadi string biasa dengan menggunakan join

print(" ".join(data))

data_string = "ando"

print(data_string[1])
print(data_string[1:])
print(data_string[1::])

# Cara memisahkan karakter yang ada di dalam string
# data_string = "ando-rika-dina"
# data_string = data_string.split(',')
# print(data_string)

# data_string = data_string.split('-',1)
# print(data_string)

# muttable
# immutable
data5 = "andozamhariro"
data2 = "i" + data5[1:]
print(data2)

data5 = "oke"

print(data5)

# Palindrom = --> okeeko -->okeeko

data = "ando"
# if data == data[::-1]:
#     print("is palindrom")
# else:
#     print("not palindrom")

data = "okeeko"
data = list(data)
data.reverse()
if data == ''. join(data):
    print("is palindrom")
else:
    print("not palindrom")

data = 'okeeko'
data2 = list(data)

data2.reverse()
data2 = ''.join(data2)

if data == data2:
    print("is palindrom")
else:
    print("bukan palindrom")

def palindrom(arg1):
    temp = list(arg1) 
    j = -1
    arg1 = list(arg1)

    for i in range(len(arg1)):
        temp[i] = arg1[j]
        j -= 1
        if data1 == ''.join(temp):
            print("its palindrom")
        else:
            print("its not palindrom")


# def is_palindrom(kata):
#     for i in range(len(kata)):
#         print(i)

# is_palindrom("kasur rusak")

def is_palindrom(kata):
    hasil =""
    for i in range(len(kata)):
        if kata[i] == kata[len(kata) - i - 1]:
            hasil += kata[i]

    if hasil == kata:
        return f"{kata} adalah palindrom"

print(is_palindrom("kasur rusak"))

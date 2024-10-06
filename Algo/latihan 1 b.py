print('Masukkan panjang menu: ')

b = int(input())

print('Jumlah inputan:', b)

list_menu = []
for i in range(b):
    print('Masukkan id menu: ')
    id = int(input())
    print("Masukkan parent menu: ")
    parent = int(input())
    print("Masukkan label menu: ")
    label = input()
    lst_tmp = [id,parent,label]
    list_menu.append(lst_tmp)

print(list_menu)

def selanjutnya(s,t):
    for i in list_menu:
        if int(i[1]) == s :
            print(("....."*t)+i[2])
            selanjutnya(int(i[0]),t + 1)
selanjutnya(0,0)


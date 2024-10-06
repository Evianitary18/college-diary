print ('Masukkan panjang menu: ')

p = int (input())

print('p: ',p)

list_menu = []
for a in range(p):
    print ('Masukkan id menu: ')
    id = int (input())
    print ('Masukkan parent menu: ')
    parent = int (input())
    print ('Masukkan label menu:')
    label = input ()
    lst_tmp = [id,parent,label]
    list_menu.append(lst_tmp)

print(list_menu)

def menu (lst_menu):
    if len(lst_menu) == 1:
        print (lst_menu[0][1])
    else:
        menu(lst_menu) 

garis = '.'*(parent)
def tampilkanAngka(p, i = 1):
    print (f'{garis} {label}')
    
    if (p<i):
        tampilkanAngka (p, i + 1)
    print (f'{garis} {label}')
tampilkanAngka (p)
'''----------------------------------------------------'''

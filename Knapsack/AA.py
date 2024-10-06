#mencari massa
mol1= mol1 = int(input('masukan besarnya mol1 ='))
mol2= mol2 = int(input('masukan besarnya mol2 ='))
mol1= mol3 = int(input('masukan besarnya mol3 ='))
mol1= mol4 = int(input('masukan besarnya mol4 ='))
mol1= mol5 = int(input('masukan besarnya mol5 ='))


seluruh_mol = mol1,mol2,mol3,mol4,mol5

mr = int(input('masukan besarnya mr='))

massa1= a = ('mol1*mr')
massa1= b = ('mol2*mr')
massa1= c = ('mol3*mr')
massa1= d = ('mol4*mr')
massa1= e = ('mol5*mr')

seluruh_massa = a,b,c,d,e

print('seluruh_massa', seluruh_mol)

masukan besarnya mol = 
masukan besarnya mol = 
masukan besarnya mol = 
masukan besarnya mol = 
masukan besarnya mol = 
masukan besarnya mr = 
seluruh_mol= (18, 36, 54, 72, 90)

import matplotlib.pylot as plt

mol = [1, 2, 3, 4, 5]
massa = [18, 36, 54, 72, 90]

import matplotlib.pyplot as plt

massa = [18, 36, 54, 72, 90]
mol = []

n = len(massa)

for i in range(n):
    mol_value = float(input("Masukkan besarnya mol ke-{}: ".format(i+1)))
    mol.append(mol_value)

plt.plot(mol, massa, 'bo-')
plt.xlabel('mol (mol)')
plt.ylabel('massa (m)')
plt.title('Grafik Hubungan antara Mol dengan Massa')
plt.grid(True)
plt.show()
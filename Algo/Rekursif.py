# # Bentuk fungsi rekursif
# def pangkatR(n, p) :
#     if p == 0:
#         return 1
#     elif p > 0:
#         return n * pangkatR(n, p - 1)
#     else:
#         return 1 / pangkatR(n, 0 - p)

# print(pangkatR(2, -2))

# Faktorial, 4! = 4*3*2*1 = 24

# def faktorialR(n):
#     if n == 1:
#         return 1
#     else:
#         hasil = n * faktorialR(n - 1)
#         print('hasil : ', hasil)
#         return hasil
    
    
# hasilFak = faktorialR(4)
# print('Fak 4 : ', hasilFak)

def pangkatR(n, p):
    if p == 0:
        return 1
    elif p > 0:
        return n * pangkat
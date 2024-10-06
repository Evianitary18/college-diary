# fungsion dalam fungsion yang membuat fungsi itu sendiri samahalnya membuat infinitive loop

# Basecase untuk mengentikan looping di rekursif

def print_halo():
    print("Ini Rekursi")
    print_halo()

# print_halo()
#  menghindari pengulangan yang berulang-ulang (FUNGSI BASE CASE)
def print_halo(base):
    if base == 1:
        return
    print("Ini Rekursi")
    print_halo(base - 1)

print_halo(5) 

 
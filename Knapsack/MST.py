import tkinter as tk
import math

window = tk.Tk()

penampung = []
with open('t1.txt') as file:
    line = file.readlines()
    for i in line:
        penampung.append(i)

penampungKedua = []
for i in penampung:
    penampungKedua.append(i.split())

jumlahTitik = int(penampungKedua[0][0])
koordinat = penampungKedua[1:]


lebar = 5000
tinggi = 4000

canvas1 = tk.Canvas(window, width=lebar, height = tinggi)
canvas1.pack()

list_terkoneksi = []
list_titik = []

def membuat_poin () :
# Membuat point secara random
    for i in range (jumlahTitik):
        var = koordinat[i]
        x = int(var[0])
        y = int(var[1])
        list_titik.append([i, x, y])
        canvas1.create_oval(x-10, y-10, x+10, y+10, fill='green')
        canvas1.create_text(x, y, text = i) 
        window.update()

    window.after(1000, menggambar_garis)

def menggambar_garis ():
    while len(list_terkoneksi) < jumlahTitik:
        # point index 0 diset sebagai terhubung/awal mulai
        if len(list_terkoneksi) == 0:
            list_terkoneksi.append(0)
            continue

        selected_point = -1
        closest_distance = 10000000
        selected_source = []
        selected_sink = []
        # mencari unconnected point yang memiliki jarak terkecil dengan point-point yang sudah terhubung
        for uc in list_titik:
            index = uc[0]
            if index in list_terkoneksi:
                continue

            x1 = uc[1]
            y1 = uc[2]

            # menghubungkan dengan point terdekat yang sudah terhubung
            for c in list_terkoneksi:
                cpoint = list_titik[c]
                x2 = cpoint[1]
                y2 = cpoint[2]

                x3 = math.pow(x2 - x1, 2)
                y3 = math.pow(y2 - y1, 2)
                jarak = math.sqrt(x3 + y3)
                # hitung jarak
                
                # simpan point jika jaraknya lebih kecil dr point sebelumnya
                if jarak < closest_distance:
                    closest_distance = jarak
                    selected_source = cpoint
                    selected_sink = uc
        
        # sudah menemukan point terdekat untuk dihubungkan
        # gambar ke gui dan simpan di list point terhubung
        list_terkoneksi.append(selected_sink[0])
        canvas1.create_line(selected_source[1], selected_source[2], selected_sink[1], selected_sink[2])
        window.update()
        
membuat_poin()



window.mainloop()
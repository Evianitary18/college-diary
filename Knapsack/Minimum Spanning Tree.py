import tkinter as tk
import math

window = tk.Tk()
canvas = tk.Canvas(window, width=1000, height=1000)
canvas.pack()
total_node = int (input())
node_list = []
list_connected =[]

def membuat_poin () :
# Membuat point secara random
    for i in range (total_node):
        node = input ()
        x = int(node.split('   ')[0])
        y = int(node.split('   ')[1])
        node_list.append([i, x, y])
        canvas.create_oval(x, y, x+30, y+30, fill='green')
        canvas.create_text(x, y, text = i+1) 

def menggambar_garis ():
    while len(list_connected) < total_node:
        # point index 0 diset sebagai terhubung/awal mulai
        if len(list_connected) == 0:
            list_connected.append(0)
            continue

        closest_distance = 10000000
        selected_source = []
        selected_sink = []
        # mencari unconnected point yang memiliki jarak terkecil dengan point-point yang sudah terhubung
        for uc in node_list:
            index = uc[0]
            if index in list_connected:
                continue

            x1 = uc[1]
            y1 = uc[2]

            # menghubungkan dengan point terdekat yang sudah terhubung
            for c in list_connected:
                cpoint = node_list[c]
                x2 = cpoint[1]
                y2 = cpoint[2]

                # hitung jarak
                jarak = math.sqrt((x1-x2)**2 + (y1 -y2)**2)
                # simpan point jika jaraknya lebih kecil dr point sebelumnya
                if jarak < closest_distance:
                    closest_distance = jarak
                    selected_source = cpoint
                    selected_sink = uc
        
        # sudah menemukan point terdekat untuk dihubungkan
        # gambar ke gui dan simpan di list point terhubung
        list_connected.append(selected_sink[0])
        canvas.create_line(selected_source[1], selected_source[2], selected_sink[1], selected_sink[2])
        # memberi text ditengah garis
        x = (selected_source[1] + selected_sink[1]) /2
        y = (selected_source[2] + selected_sink[2]) /2
        canvas.create_text(x, y, text=len(list_connected)-1)
membuat_poin()
menggambar_garis()
# print(list_connected)


window.mainloop()

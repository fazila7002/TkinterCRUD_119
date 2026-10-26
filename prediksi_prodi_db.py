# Nama  : Fazilatun Nisa Muslimah
# NIM   : 20250140119
# Kelas : C

import tkinter as tk


WARNA_BG = "#F4F6FB"
WARNA_HEADER = "#1F3A93"
WARNA_HASIL = "#0B7A3E"


root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.configure(bg=WARNA_BG, padx=20, pady=20)
root.resizable(False, False)

judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan",
                 font=("Segoe UI", 18, "bold"), fg="white", bg=WARNA_HEADER,
                 padx=20, pady=10)
judul.grid(row=0, column=0, sticky="ew", pady=(0, 15))

frame_input = tk.LabelFrame(root, text=" Masukkan Data Siswa ",
                            font=("Segoe UI", 10, "bold"), bg=WARNA_BG,
                            padx=15, pady=10)
frame_input.grid(row=1, column=0, sticky="ew")

labels = ["Nama Siswa", "Nilai Biologi", "Nilai Fisika", "Nilai Inggris"]
entries = []
for i, teks in enumerate(labels):
    tk.Label(frame_input, text=teks, font=("Segoe UI", 10), bg=WARNA_BG,
             anchor="w", width=14).grid(row=i, column=0, sticky="w", pady=5)
    e = tk.Entry(frame_input, width=30, bd=2, font=("Segoe UI", 10))
    e.grid(row=i, column=1, pady=5)
    entries.append(e)
entry_nama, entry_biologi, entry_fisika, entry_inggris = entries

root.mainloop()

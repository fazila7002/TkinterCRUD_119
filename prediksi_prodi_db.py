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

root.mainloop()

# Nama  : Fazilatun Nisa Muslimah
# NIM   : 20250140119
# Kelas : C

import os
import sqlite3
import tkinter as tk


# database nya disimpan di folder yg sama kayak file ini
DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nilai_siswa.db")


def run_query(sql, params=()):
    conn = sqlite3.connect(DB_NAME)
    try:
        with conn:  # otomatis commit
            return conn.execute(sql, params).fetchall()
    finally:
        conn.close()


# nilai paling tinggi yg nentuin fakultasnya
def prediksi_fakultas(biologi, fisika, inggris):
    if biologi >= fisika and biologi >= inggris:
        return "Kedokteran"
    elif fisika >= biologi and fisika >= inggris:
        return "Teknik"
    else:
        return "Bahasa"


WARNA_BG = "#F4F6FB"
WARNA_HEADER = "#1F3A93"
WARNA_HASIL = "#0B7A3E"


def submit_nilai():
    nama = entry_nama.get()
    bio = int(entry_biologi.get())
    fis = int(entry_fisika.get())
    ing = int(entry_inggris.get())

    hasil = prediksi_fakultas(bio, fis, ing)
    hasil_var.set(f"Prediksi fakultas {nama}: {hasil}")


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

tombol = tk.Button(root, text="Submit Nilai", command=submit_nilai,
                   font=("Segoe UI", 11, "bold"), bg=WARNA_HEADER, fg="white",
                   activebackground="#2C4FBF", activeforeground="white",
                   padx=20, pady=5, cursor="hand2")
tombol.grid(row=2, column=0, pady=15)

hasil_var = tk.StringVar(value="Hasil prediksi akan tampil di sini")
tk.Label(root, textvariable=hasil_var, font=("Segoe UI", 12, "bold"),
         fg=WARNA_HASIL, bg="white", relief=tk.GROOVE, padx=10, pady=10
         ).grid(row=3, column=0, sticky="ew")

root.mainloop()

##Melanjutkan dari Praktikum Sebelumnya:
##Menambahkan kondisi nilaiyang berbeda untuk setiap pilihan prodi yang diinginkan
##Menambahkanpenyimpanan data keSQLLite
##Buat table nilai_siswa
##Buat atribut yang berisi nama_siswa, biologi, fisika, inggris, prediksi_fakultas
##Buat entry menggunakan tkinter untuk nama siswa, biologi, fisika, dan inggris
##Jika nilai Biologi paling tinggi, maka hasil prediksi = Kedokteran
##Jika nilai Fisika paling tinggi, maka hasil prediksi = Teknik
##Jika nilai Inggris paling tinggi, maka hasil prediksi = Bahasa
##Terdapat button tkinter untuk submit nilai
import sqlite3
import tkinter as tk
from tkinter import messagebox

DB_NAME = "nilai_siswa.db"

def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Nama tabel disesuaikan menjadi 'nilai_siswa'
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi INTEGER NOT NULL,
            fisika INTEGER NOT NULL,
            inggris INTEGER NOT NULL,
            prediksi_fakultas TEXT NOT NULL
        )    
    """)
    conn.commit()
    conn.close()

def prediksi_fakultas(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        return "Teknik"
    elif inggris > biologi and inggris > fisika:
        return "Bahasa"
    else:
        return "Tidak Dapat Ditentukan"

def submit_nilai():
    nama = ent_nama.get().strip()
    try:
        bio = int(ent_biologi.get().strip())
        fis = int(ent_fisika.get().strip())
        ing = int(ent_inggris.get().strip())
    except ValueError:
        messagebox.showerror("ERROR!", "Nilai harus berupa angka!")
        return
        
    if not nama:
        messagebox.showerror("ERROR!", "Nama siswa tidak boleh kosong!")
        return
    
    hasil_prediksi = prediksi_fakultas(bio, fis, ing)

    # Simpan ke tabel 'nilai_siswa'
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    """, (nama, bio, fis, ing, hasil_prediksi))
    conn.commit()
    conn.close()

    # Update tampilan label hasil di GUI & tampilkan pop-up
    label_hasil.config(text=f"Hasil Prediksi: {hasil_prediksi}")
    messagebox.showinfo("Hasil Prediksi", f"Prediksi Fakultas: {hasil_prediksi}")

    # Reset form input
    ent_nama.delete(0, tk.END)
    ent_biologi.delete(0, tk.END)
    ent_fisika.delete(0, tk.END)
    ent_inggris.delete(0, tk.END)

# Inisialisasi Database sebelum GUI berjalan
create_db() 

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x520")
root.configure(bg="#2A1B3D")

label_judul = tk.Label(
    root, 
    text="Aplikasi Prediksi Prodi Pilihan", 
    font=("Arial", 14, "bold"),
    bg="#2A1B3D",
    fg="#FFD700"
)
label_judul.pack(pady=15)

frame_input = tk.Frame(root, bg="#3B224C", padx=15, pady=15)
frame_input.pack(pady=10, padx=20)

lbl_nama = tk.Label(frame_input, text="Nama Siswa:", bg="#3B224C", fg="#FFD700", font=("Arial", 9, "bold"))
lbl_nama.grid(row=0, column=0, sticky="w", pady=5, padx=5)
ent_nama = tk.Entry(frame_input, width=15, bg="#1E122B", fg="#FFD700", insertbackground="#FFD700", bd=1)
ent_nama.grid(row=0, column=1, pady=5, padx=5)

lbl_biologi = tk.Label(frame_input, text="Nilai Biologi:", bg="#3B224C", fg="#FFD700", font=("Arial", 9, "bold"))
lbl_biologi.grid(row=1, column=0, sticky="w", pady=5, padx=5)
ent_biologi = tk.Entry(frame_input, width=15, bg="#1E122B", fg="#FFD700", insertbackground="#FFD700", bd=1)
ent_biologi.grid(row=1, column=1, pady=5, padx=5)

lbl_fisika = tk.Label(frame_input, text="Nilai Fisika:", bg="#3B224C", fg="#FFD700", font=("Arial", 9, "bold"))
lbl_fisika.grid(row=2, column=0, sticky="w", pady=5, padx=5)
ent_fisika = tk.Entry(frame_input, width=15, bg="#1E122B", fg="#FFD700", insertbackground="#FFD700", bd=1)
ent_fisika.grid(row=2, column=1, pady=5, padx=5)

lbl_inggris = tk.Label(frame_input, text="Nilai Inggris:", bg="#3B224C", fg="#FFD700", font=("Arial", 9, "bold"))
lbl_inggris.grid(row=3, column=0, sticky="w", pady=5, padx=5)
ent_inggris = tk.Entry(frame_input, width=15, bg="#1E122B", fg="#FFD700", insertbackground="#FFD700", bd=1)
ent_inggris.grid(row=3, column=1, pady=5, padx=5)

btn_prediksi = tk.Button(
    root, 
    text="Submit Nilai / Hasil Prediksi", 
    command=submit_nilai,
    bg="#4A2E5D",
    fg="#FFD700",
    activebackground="#FFD700",
    activeforeground="#2A1B3D",
    font=("Arial", 10, "bold"),
    cursor="hand2"
)
btn_prediksi.pack(pady=15)

# Label Luaran Hasil Prediksi
label_hasil = tk.Label(
    root, 
    text="Hasil Prediksi: -", 
    font=("Arial", 11, "bold"),
    bg="#2A1B3D",
    fg="#FFD700"
)
label_hasil.pack(pady=5)

root.mainloop()
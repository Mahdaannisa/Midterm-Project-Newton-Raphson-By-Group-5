# PROJECT-GROUP 5

**UTS PRAKTIKUM KOMPUTASI NUMERIK**

ANGGOTA KELOMPOK 5:
1. MAHDA ANNISA (2408107010036)
2. AR RAUDHATUL PUTRI MUHIDA (2408107010082)
3. ARSHA ALIFA MAHMUD (2408107010095)
4. MUHAMMAD SHIDQI HANIF (2408107010096)
5. NAYLA KHANSA LIVYA (2408107010098)
6. AHMAD HANIF (2408107010114)

# Newton-Raphson Method (Numerical Computation Project)

## 📌 Deskripsi
Proyek ini mengimplementasikan **Metode Newton-Raphson** untuk mencari akar persamaan non-linear menggunakan Python.  
Metode Newton-Raphson adalah prosedur iteratif yang menggunakan garis singgung fungsi untuk memperkirakan letak akar dari suatu persamaan \( f(x) = 0 \).  

Aplikasi ini dilengkapi dengan **GUI (Graphical User Interface)** sehingga pengguna dapat dengan mudah:
- Memasukkan fungsi \( f(x) \), nilai awal \( x_0 \), jumlah iterasi, dan galat (\( \varepsilon \)).
- Menjalankan perhitungan metode Newton-Raphson.
- Melihat hasil iterasi dalam bentuk tabel.
- Menampilkan grafik fungsi dan proses pencarian akar.

---

## ⚙️ Metode Newton-Raphson
1. Tentukan fungsi f(x) dan turunan pertamanya f'(x).  
2. Masukkan nilai tebakan awal x₀.  
3. Tentukan toleransi error ε (misalnya 0.0001).  
4. Lakukan iterasi dengan rumus: `x_(n+1) = x_n - f(x_n)/f'(x_n)`.  
5. Iterasi berhenti jika `|x_(n+1) - x_n| < ε`.
 
---

## 📂 Struktur Proyek
- **`main.py`** → Program utama untuk menjalankan aplikasi GUI Newton-Raphson.  
- **`app.py`** → Antarmuka pengguna (GUI), tempat input fungsi, nilai awal, iterasi, dan error.  
- **`formatter.py`** → Modul untuk memformat input & output agar bisa diproses Python dan ditampilkan rapi.  
- **`newton.py`** → Logika utama metode Newton-Raphson (perhitungan iterasi, turunan, galat).  
- **`plotter.py`** → Menampilkan grafik fungsi & posisi akar secara visual.  

---

## 📂 Penjelasan Singkat Kode

1. **main.py**  
   Fungsi: Entry point (program utama). Isinya biasanya cuma menjalankan app.py (GUI). Jadi saat user jalankan `python main.py`, program langsung membuka aplikasi Newton-Raphson.  

2. **app.py**  
   Fungsi: Membuat GUI (Graphical User Interface). User bisa input fungsi f(x), tebakan awal x₀, jumlah iterasi, dan error toleransi (ε). Output yang ditampilkan berupa tabel hasil iterasi dan grafik fungsi dengan posisi akar.  

3. **formatter.py**  
   Fungsi: Memformat input dan output. Contoh: user menulis `x^2 - 4`, lalu file ini mengubahnya menjadi format Python `x**2 - 4`. Output angka juga diformat agar lebih rapi.  

4. **newton.py**  
   Fungsi: Inti perhitungan metode Newton-Raphson. Menggunakan rumus `x_next = x - f(x)/f_prime(x)`. Proses dilakukan berulang sampai error < toleransi, lalu hasilnya dikembalikan sebagai akar hampiran.  

5. **plotter.py**  
   Fungsi: Visualisasi grafik. Menampilkan kurva f(x) dan posisi akar yang ditemukan, sehingga user bisa melihat proses pencarian akar secara visual.  

---

## ▶️ Cara Menjalankan
1. Clone repositori ini:
   ```bash
   git clone https://github.com/Mahdaannisa/Midterm-Project-Newton-Raphson-By-Group-5.git


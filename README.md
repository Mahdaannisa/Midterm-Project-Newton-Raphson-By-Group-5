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
1. Tentukan fungsi \( f(x) \) dan turunan pertamanya \( f'(x) \).
2. Masukkan nilai tebakan awal \( x_0 \).
3. Tentukan toleransi error \( \varepsilon \) (misalnya 0.0001).
4. Lakukan iterasi dengan rumus:
   \[
   x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
   \]
5. Iterasi berhenti jika \( |x_{n+1} - x_n| < \varepsilon \).

---

## 📂 Struktur Proyek
- **`main.py`** → Program utama untuk menjalankan aplikasi GUI Newton-Raphson.  
- **`app.py`** → Antarmuka pengguna (GUI), tempat input fungsi, nilai awal, iterasi, dan error.  
- **`formatter.py`** → Modul untuk memformat input & output agar bisa diproses Python dan ditampilkan rapi.  
- **`newton.py`** → Logika utama metode Newton-Raphson (perhitungan iterasi, turunan, galat).  
- **`plotter.py`** → Menampilkan grafik fungsi & posisi akar secara visual.  

---

## ▶️ Cara Menjalankan
1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/nama-repo.git


# 📸 Auto Screenshot Praktikum PHP

Skrip Python untuk mengambil screenshot otomatis file PHP dari project web lokal, menampilkan kode di **VSCode** (sisi kiri) dan hasil browser (sisi kanan) secara berdampingan dalam satu layar.

---

## ✨ Fitur

- Otomatis membuka setiap file `.php` di VSCode dan browser secara bersamaan
- Mengatur layout split-screen (VSCode kiri, browser kanan) secara otomatis
- Menyimpan screenshot setiap file dengan nama yang terurut dan rapi
- Mendukung struktur folder PHP bertingkat (recursive)
- Membuka folder output secara otomatis setelah selesai

---

## 🔧 Requirements

- Windows 10 / 11
- Python 3.8+
- Web server lokal (misalnya: [Laragon](https://laragon.org/), [XAMPP](https://www.apachefriends.org/), [WAMP](https://www.wampserver.com/), dll.)
- [Visual Studio Code](https://code.visualstudio.com/) (dengan perintah `code` tersedia di PATH)
- Browser pilihan (Chrome, Firefox, Brave, Edge, dll.)

---

## 📦 Instalasi

### 1. Clone repositori

```bash
git clone https://github.com/username/Auto-Screenshot-Praktikum-PHP.git
cd Auto-Screenshot-Praktikum-PHP
```

### 2. Buat virtual environment (opsional, tapi disarankan)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependensi

```bash
pip install -r requirements.txt
```

### 4. Pastikan VSCode bisa dijalankan lewat terminal

Cek dengan perintah:
```bash
code --version
```
Jika belum bisa, tambahkan VSCode ke PATH melalui **Settings → Add to PATH** di installer VSCode, atau tambahkan secara manual ke PATH sistem:
```
C:\Users\<nama_user>\AppData\Local\Programs\Microsoft VS Code\bin
```

---

## ⚙️ Konfigurasi

Buka file `auto_screenshot_praktikum_php.py` dan sesuaikan bagian **KONFIGURASI** di baris atas:

```python
PHP_FOLDER      = r"C:\xampp\htdocs\praktikum"       # Folder project PHP kamu
OUTPUT_FOLDER   = r"C:\xampp\htdocs\output"           # Folder hasil screenshot
LOCALHOST_BASE  = "http://localhost/praktikum"         # URL base sesuai web server lokal kamu
BROWSER_EXE     = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path ke browser pilihanmu
DELAY_BROWSER   = 1   # Detik tunggu browser load (naikkan jika lambat)
DELAY_VSCODE    = 1   # Detik tunggu VSCode buka file
```

> **Catatan:** Pastikan web server lokal kamu sudah berjalan sebelum menjalankan skrip.

### Contoh path browser umum

| Browser | Path Default |
|---|---|
| Google Chrome | `C:\Program Files\Google\Chrome\Application\chrome.exe` |
| Mozilla Firefox | `C:\Program Files\Mozilla Firefox\firefox.exe` |
| Microsoft Edge | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` |
| Brave | `C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe` |

### Contoh konfigurasi web server lokal

| Web Server | `PHP_FOLDER` | `LOCALHOST_BASE` |
|---|---|---|
| XAMPP | `C:\xampp\htdocs\praktikum` | `http://localhost/praktikum` |
| Laragon | `C:\laragon\www\praktikum` | `http://localhost/praktikum` |
| WAMP | `C:\wamp64\www\praktikum` | `http://localhost/praktikum` |

---

## ▶️ Cara Menjalankan

```bash
python main.py
```

Skrip akan:
1. Mencari semua file `.php` di `PHP_FOLDER` secara rekursif
2. Membuka tiap file di VSCode dan browser secara bergantian
3. Mengatur posisi jendela split-screen otomatis
4. Mengambil screenshot dan menyimpannya ke `OUTPUT_FOLDER`
5. Membuka folder output setelah semua file selesai diproses

---

## 📁 Struktur Output

Screenshot disimpan dengan format penamaan:

```
001_nama_file.png
002_nama_file.png
003_nama_file.png
...
```

---

## ❓ Troubleshooting

| Masalah | Solusi |
|---|---|
| Window VSCode/browser tidak terdeteksi | Naikkan nilai `DELAY_BROWSER` atau `DELAY_VSCODE` |
| Halaman PHP tidak muncul di browser | Pastikan web server lokal sudah aktif dan URL sudah benar |
| `code` tidak dikenali di terminal | Tambahkan VSCode ke PATH sistem |
| Browser tidak terbuka | Periksa kembali nilai `BROWSER_EXE`, pastikan path sudah benar |

---

## 📄 Lisensi

Proyek ini menggunakan lisensi [MIT](LICENSE).
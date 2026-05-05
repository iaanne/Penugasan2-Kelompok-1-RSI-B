# 🗂️ Penugasan Praktikum 2 RSI – Penugasan CRUD

Repo ini dibuat untuk memenuhi **Penugasan Praktikum 2**

---

## 👥 Anggota Kelompok

| No | Nama | NIM |
|----|------|-----|
| 1 | Stefani Ayudya Prasetyo | L0224011 |
| 2 | Jocelyn Louisa | L0224034 |
| 3 | Talitha Sukma Mahardika | L0224037 |
| 4 | Adrian Farrel Aziz Yatyoga | L0224040 |

---
# 🛠️ Penugasan 2 – Backend Setup & API Development

Repositori ini berisi fondasi utama sistem backend yang dibangun dengan arsitektur berlapis (Layered Architecture), integrasi database relasional, dan sistem migrasi otomatis.

## 📌 Fitur & Implementasi

### ⚙️ 1. Setup Backend & Database Connection
- Pengembangan menggunakan framework Python (seperti FastAPI/Flask).
- Koneksi database relasional dikonfigurasi secara aman melalui file `.env`.

### 🧬 2. Database Migration dengan Alembic
- Menggunakan **Alembic** untuk manajemen versi skema database.
- Automasi pembuatan tabel berdasarkan model entitas yang telah dirancang.
- Memastikan konsistensi struktur data di seluruh lingkungan pengembangan.

### 🗂️ 3. Arsitektur Berlapis (Layered Architecture)
Kode diorganisir secara modular untuk skalabilitas dan pemeliharaan yang mudah:
- **Repository**: Abstraksi akses database (Query, Insert, Update, Delete).
- **Service**: Tempat implementasi logika bisnis utama.
- **Controller**: Handler untuk request/response HTTP (API Endpoints).
- **DTO (Data Transfer Object)**: Validasi skema data untuk input dan output API.

### 🧩 4. Model & Entitas (Schema)
Implementasi tabel database yang saling berelasi:
- **User / Account / Role**: Manajemen identitas dan otoritas.
- **Event**: Informasi acara atau kegiatan.
- **Registration**: Pencatatan partisipasi user dalam event.

### 🔗 5. Implementasi Endpoint CRUD
Pembuatan API Endpoint lengkap untuk entitas utama:
- **GET**: Pengambilan data.
- **POST**: Pembuatan data baru.
- **PUT/PATCH**: Pembaruan data yang ada.
- **DELETE**: Penghapusan data.

### 📄 6. Dokumentasi API (Swagger)
- Dokumentasi otomatis tersedia melalui endpoint `/docs`.
- Mencakup pengujian skenario **Success** dan **Failed** untuk validasi fungsionalitas.
- Hasil pengujian telah didokumentasikan dalam format PDF.

---

## 🚀 Hasil Akhir
1. **Ready-to-Use API**: Backend berjalan stabil di lingkungan lokal.
2. **Scalable Code**: Struktur kode yang rapi dan mudah dikembangkan.
3. **Managed Database**: Skema database yang terkelola dengan baik melalui migration tools.

---

## 🔧 Panduan Git untuk Anggota

> Gunakan **Git Bash** untuk semua perintah berikut.

### 1. Clone Repository *(sekali saja di awal)*
```bash
git clone https://github.com/iaanne/Penugasan2-Kelompok-1-RSI-B.git
cd Penugasan2-Kelompok-1-RSI-B
```

### 2. Buat Branch Pribadi
```bash
git checkout -b nama-kamu   # contoh: git checkout -b ian
```

### 3. Sebelum Mulai Kerja — Selalu Pull Dulu
```bash
git pull origin main
```

### 4. Simpan Perubahan
```bash
git add .
git commit -m "ubah frontend"
git push -u origin nama-kamu
```

### 5. Buat Pull Request (PR)
- Buka repo di GitHub
- Klik **"Compare & Pull Request"**
- Isi deskripsi → klik **Create Pull Request**

---

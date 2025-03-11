# hunting.py
automated pentesting tools
🔍 Hunting.py - Automasi Pentesting Subdomain
📌 Deskripsi
hunting.py adalah tool otomatisasi pentesting subdomain berbasis Python, yang mempermudah proses pencarian dan scanning subdomain.
Tool ini secara otomatis melakukan:

🔎 Mencari subdomain menggunakan Subfinder
✅ Mengecek subdomain aktif menggunakan Httpx
🔥 Melakukan scanning keamanan menggunakan Nuclei
Tool ini sangat cocok digunakan untuk bug bounty hunters, pentesters, dan security researchers yang ingin mempercepat proses pentesting subdomain.

📂 Struktur Hasil Scan
📄 {target}.txt → Daftar subdomain yang ditemukan
📄 active{target}.txt → Daftar subdomain yang aktif
📄 nucactive{target}.txt → Hasil scan keamanan dari Nuclei

🛠 Instalasi
Sebelum menjalankan tool ini, pastikan sudah menginstal Go dan Python 3 di sistemmu.

1️⃣ Clone Repository
bash
Copy
Edit
git clone https://github.com/phims403/reponame.git
cd reponame
2️⃣ Jalankan Script
bash
Copy
Edit
python3 hunting.py
3️⃣ Masukkan Target
bash
Copy
Edit
Masukkan domain target: example.com
⚡ Cara Kerja
Mengecek dependencies: Tool akan memverifikasi apakah subfinder, httpx, dan nuclei sudah terinstall. Jika belum, tool akan menginstallnya otomatis.
Subdomain Enumeration: Menggunakan Subfinder untuk mencari subdomain.
Subdomain Validation: Mengecek subdomain yang aktif menggunakan Httpx.
Security Scanning: Melakukan scanning keamanan pada subdomain aktif menggunakan Nuclei.
📜 Lisensi
Tool ini bersifat open-source dan dibuat untuk tujuan edukasi serta pentesting yang sah. Penggunaan untuk aktivitas ilegal dilarang. 🚀


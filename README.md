Hunting Tool v0.3.1

Hunting Tool v0.3.1 adalah alat otomatisasi untuk bug bounty hunter dan pentester yang menggabungkan beberapa tool populer untuk reconnaissance dan vulnerability scanning. Dengan tool ini, Anda bisa dengan mudah menemukan subdomain, mengecek statusnya, serta memindai celah keamanan menggunakan Nuclei.


⚠️ Disclaimer

Hunting Tool v0.3.1 dibuat untuk tujuan edukasi dan penelitian keamanan siber. Pengguna diharapkan untuk:

1. Menggunakan alat ini secara etis

2. Mematuhi hukum yang berlaku – Penggunaan alat ini untuk menyerang sistem tanpa izin dapat melanggar undang-undang terkait keamanan siber di negara Anda.

3. Tidak menyalahgunakan alat ini – Hunting Tool bukan alat untuk peretasan ilegal, melainkan untuk membantu bug bounty hunter dan pentester dalam menemukan celah keamanan yang dilaporkan secara etis.

🛑 Tanggung Jawab Pengguna

Kami tidak bertanggung jawab atas segala bentuk penyalahgunaan alat ini. Pengguna bertanggung jawab penuh atas tindakan yang mereka lakukan menggunakan Hunting Tool v0.3.1.

Jika Anda tidak yakin apakah suatu tindakan diperbolehkan, silakan baca kebijakan bug bounty program yang bersangkutan atau konsultasikan dengan ahli hukum sebelum menggunakan tool ini.

Gunakan dengan bijak dan tetap etis dalam berburu bug! 🚀



🚀 Fitur Utama
✅ Subdomain Enumeration – Mencari subdomain aktif menggunakan Subfinder
✅ Live Host Checker – Mengecek subdomain yang aktif menggunakan Httpx
✅ Automated Vulnerability Scanning – Memindai celah keamanan dengan Nuclei
✅ List Program Bug Bounty – Termasuk daftar URL open bug bounty dari HackerOne, BugCrowd, dan YesWeHack
✅ Auto-Update System – Memastikan semua tool dalam keadaan terbaru
✅ Output Tersimpan – Semua hasil akan tersimpan untuk analisis lebih lanjut

INSTALASI

Tool ini menggunakan beberapa dependency penting. Catatan: Tool ini tidak mendukung Termux karena keterbatasan Golang dan dependensi lainnya.

Jika Go belum terinstall, silakan instal terlebih dahulu:

sudo apt update && sudo apt install golang -y
(Untuk Debian/Ubuntu)
brew install go
(Untuk macOS)

# Clone repository
git clone https://github.com/phims403/huntingtool.git
cd huntingtool

# Berikan izin eksekusi (untuk bash)
chmod +x hunting.sh

# Jalankan script (untuk bash)
./hunting.sh

# Jalankan script (untuk python)
python hunting.py

🎯 Cara Penggunaan

1. Menjalankan Hunting Tool

Cukup jalankan script berikut dan masukkan domain target:

Tool akan melakukan:
1️⃣ Mencari subdomain menggunakan Subfinder
2️⃣ Mengecek subdomain aktif dengan Httpx
3️⃣ Melakukan pemindaian kerentanan menggunakan Nuclei

2. Format Output

Hasil akan disimpan dalam beberapa file:
📂 target.txt → Daftar semua subdomain yang ditemukan
📂 active_target.txt → Daftar subdomain yang aktif
📂 nuc_active_target.txt → Hasil pemindaian dengan Nuclei

🛠️ Tools yang Digunakan

Hunting Tool mengandalkan beberapa alat berikut:
🔹 Subfinder → Enumerasi subdomain secara otomatis
🔹 Httpx → Mengecek status live host
🔹 Nuclei → Pemindaian kerentanan berdasarkan template terbaru

Jika tool (seperti subfinder, httpx, nuclei) belum terinstal, script akan otomatis menginstalnya menggunakan Go.


📝 Contoh Penggunaan

1. Pemindaian domain example.com

bash:
./hunting.sh
Masukkan target (contoh: example.com): example.com

ptyhon:
python hunting.py
Masukkan target (contoh: example.com): example.com

Setelah proses selesai, file hasil akan tersedia di direktori yang sama.
🔗 Program Bug Bounty yang Didukung
Hunting Tool v0.3.1 juga menyediakan daftar URL program bug bounty dari:
🟢 HackerOne
🟢 BugCrowd
🟢 YesWeHack
🟢 Intigriti
🟢 Hackenproof


💡 Tips untuk Bug Bounty Hunter

✅ Pastikan target Anda menerima pengujian keamanan dengan melihat TOS dari program bug bounty
✅ Gunakan VPN atau VPS untuk menjaga privasi saat melakukan pentesting
✅ Selalu update tool dan template Nuclei untuk mendapatkan hasil yang lebih akurat
✅ Baca dokumentasi masing-masing tool untuk eksplorasi lebih lanjut

🤝 Kontribusi & Pengembangan

Jika ingin berkontribusi atau memberikan saran, silakan buat pull request atau issue di GitHub!

🔗 GitHub Repo: https://github.com/phims403/huntingtool

📩 Kontak: ehphims@example.com

🚀 Mulai berburu bug dan temukan celah keamanan dengan Hunting Tool v0.3.1!

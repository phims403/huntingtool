Berikut adalah versi yang lebih rapi, profesional, dan mudah dipahami untuk GitHub:


---

Installation Guide for Hunting Tool

Tool ini menggunakan beberapa dependency penting.
Catatan: Tool ini tidak mendukung Termux karena keterbatasan Golang dan dependensi lainnya.


---

Prasyarat

Sebelum menjalankan tool, pastikan kamu sudah menginstal:

Golang
Diperlukan untuk menginstal tools dari ProjectDiscovery seperti subfinder, httpx, dan nuclei.

Python & Pip
Diperlukan jika kamu menggunakan versi Python dari tool ini.

Git
Dibutuhkan untuk meng-clone repository tool ini.

Paket Tambahan (Opsional, tapi direkomendasikan):

curl, unzip (digunakan untuk mengunduh dan mengekstrak file bila diperlukan).




---

Langkah-langkah Instalasi

1. Install Golang

Linux (Ubuntu/Debian)

sudo apt update && sudo apt install golang -y
go version

macOS (Homebrew)

brew install go
go version

Windows

1. Download installer Golang dari https://go.dev/dl/.


2. Jalankan installer dan ikuti instruksi, pastikan untuk menambahkan Golang ke PATH.


3. Verifikasi instalasi dengan menjalankan:

go version



> Catatan: Pastikan direktori instalasi go install (biasanya $HOME/go/bin atau %USERPROFILE%\go\bin) sudah ada di PATH.




---

2. Install Python & Pip

Linux/macOS

sudo apt install python3 python3-pip -y
python3 --version
pip3 --version

Windows

1. Download installer Python dari https://www.python.org/downloads/.


2. Saat instalasi, centang opsi "Add Python to PATH".


3. Verifikasi instalasi:

python --version
pip --version




---

3. Install Git

Linux (Ubuntu/Debian)

sudo apt update && sudo apt install git -y
git --version

macOS (Homebrew)

brew install git
git --version

Windows

1. Download Git dari https://git-scm.com/downloads.


2. Jalankan installer dan ikuti petunjuk.


3. Verifikasi instalasi dengan membuka Command Prompt atau Git Bash:

git --version




---

4. Install Dependensi Tambahan (Opsional)

Linux/macOS

sudo apt install curl unzip -y

Windows

Gunakan Chocolatey untuk menginstal curl dan unzip:

choco install curl unzip -y

> Jika Chocolatey belum terinstal, lihat https://chocolatey.org.




---

Menjalankan Tool

Clone Repository

Gunakan Git untuk meng-clone repository:

git clone https://github.com/phims403/huntingtool.git
cd huntingtool

Pilih Versi Tool

Tool ini tersedia dalam dua versi: Python dan Bash. Pilih sesuai kebutuhan.

A. Versi Python

Jalankan dengan perintah berikut:

Linux/macOS:

python hunting.py

Windows:

python hunting.py


B. Versi Bash

Berikan izin eksekusi terlebih dahulu, lalu jalankan:

chmod +x hunting.sh
./hunting.sh


---

Cara Penggunaan Tool

1. Jalankan tool sesuai versi yang kamu pilih (Python atau Bash).


2. Input Target:
Saat diminta, masukkan domain target (misalnya: example.com).

> Pastikan kamu memiliki izin untuk melakukan pengujian pada domain tersebut.




3. Hasil Output:

example.com.txt → File daftar subdomain.

active_example.com.txt → File daftar subdomain yang aktif.

nuc_active_example.com.txt → File hasil scan keamanan dari Nuclei.





---

Troubleshooting

Golang Tidak Terdeteksi
Pastikan direktori Go ($HOME/go/bin atau %USERPROFILE%\go\bin) sudah ditambahkan ke PATH.
Contoh di Linux/macOS:

export PATH=$HOME/go/bin:$PATH
source ~/.bashrc

Permission Issues (Bash)
Jika terjadi error permission, pastikan script memiliki izin eksekusi:

chmod +x hunting.sh

Verifikasi Versi Dependency
Pastikan instalasi dependency berhasil dengan menjalankan:

go version
python --version
pip --version
git --version

---

Credits

Created by PHIMS

GitHub: https://github.com/phims403

Instagram: https://instagram.com/aier_phims


Gunakan tool ini secara bertanggung jawab dan hanya pada domain yang kamu memiliki izin untuk dites.

Dengan panduan di atas, kamu dapat menjalankan tool ini dengan lancar di Linux, macOS, maupun Windows.
Selamat berburu celah, dan semoga sukses!

import os
import subprocess
import shutil

# Definisikan tools dan repository instalasinya sesuai dengan GitHub ProjectDiscovery
TOOLS = {
    "subfinder": "github.com/projectdiscovery/subfinder/v2/cmd/subfinder",
    "httpx": "github.com/projectdiscovery/httpx/cmd/httpx",
    "nuclei": "github.com/projectdiscovery/nuclei/v2/cmd/nuclei"
}

def check_and_install_tools():
    for tool, repo in TOOLS.items():
        if not shutil.which(tool):
            print(f"[⚠️] {tool} belum terinstall. Menginstall...")
            install_cmd = f"go install -v {repo}@latest"
            result = subprocess.run(install_cmd, shell=True)
            if result.returncode != 0:
                print(f"[❌] Gagal menginstall {tool}. Pastikan Go sudah terinstall dan PATH sudah diset.")
            else:
                print(f"[✅] {tool} berhasil diinstall.")
        else:
            print(f"[✅] {tool} sudah terinstall.")

def update_tools():
    print("[🔄] Mengecek update untuk semua tools...")
    for tool in TOOLS:
        # Pastikan setiap tool mendukung flag update
        update_cmd = f"{tool} -update"
        subprocess.run(update_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Update template untuk Nuclei
    subprocess.run("nuclei -update-templates", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("[✅] Semua tools telah diperbarui.")

def show_banner():
    os.system("clear" if os.name == "posix" else "cls")
    print("\n🔥 Welcome to Hunting Tool 🔥\n")
    print("""
 /$$   /$$                       /$$     /$$                             /$$                         /$$
| $$  | $$                      | $$    |__/                            | $$                        | $$
| $$  | $$ /$$   /$$ /$$$$$$$  /$$$$$$   /$$ /$$$$$$$   /$$$$$$        /$$$$$$    /$$$$$$   /$$$$$$ | $$
| $$$$$$$$| $$  | $$| $$__  $$|_  $$_/  | $$| $$__  $$ /$$__  $$      |_  $$_/   /$$__  $$ /$$__  $$| $$
| $$__  $$| $$  | $$| $$  \ $$  | $$    | $$| $$  \ $$| $$  \ $$        | $$    | $$  \ $$| $$  \ $$| $$
| $$  | $$| $$  | $$| $$  | $$  | $$ /$$| $$| $$  | $$| $$  | $$        | $$ /$$| $$  | $$| $$  | $$| $$
| $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/| $$| $$  | $$|  $$$$$$$        |  $$$$/|  $$$$$$/|  $$$$$$/| $$
|__/  |__/ \______/ |__/  |__/   \___/  |__/|__/  |__/ \____  $$         \___/   \______/  \______/ |__/
                                                       /$$  \ $$                                        
                                                      |  $$$$$$/                                        
                                                       \______/                                         
    """)
    print("📌 By PHIMS")
    print("🔗 GitHub: https://github.com/username")
    print("📷 Instagram: https://instagram.com/username\n")

def main():
    check_and_install_tools()
    update_tools()
    show_banner()

    target = input("Masukkan target (contoh: example.com): ").strip()
    if not target:
        print("[❌] Target tidak boleh kosong!")
        return

    subdomain_file = f"{target}.txt"
    active_file = f"active_{target}.txt"
    nuclei_output = f"nuc_active_{target}.txt"

    print("[🔍] Mencari subdomain...")
    subprocess.run(f"subfinder -d {target} -o {subdomain_file}", shell=True)

    print("[🌐] Mengecek subdomain yang aktif...")
    subprocess.run(f"httpx -l {subdomain_file} -o {active_file}", shell=True)

    print("[🚀] Menjalankan Nuclei scan...")
    # Perintah scan nuclei tanpa flag '-ept ssl' karena tidak dikenali
    subprocess.run(f"nuclei -l {active_file} -severity low,medium,high,critical -o {nuclei_output}", shell=True)

    print("[✅] Semua proses selesai!")

if __name__ == "__main__":
    main()

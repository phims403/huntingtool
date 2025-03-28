import os
import subprocess
import shutil
# Definisikan tools dan repository instalasinya sesuai dengan GitHub ProjectDiscovery
TOOLS = {
    "subfinder": "github.com/projectdiscovery/subfinder/v2/cmd/subfinder",
    "httpx": "github.com/projectdiscovery/httpx/cmd/httpx",
    "nuclei": "github.com/projectdiscovery/nuclei/v2/cmd/nuclei"
}

    # Folder output
OUTPUT_FOLDER_SUBDO = "subdomain"
OUTPUT_FOLDER_ACTIVE = "active"
OUTPUT_FOLDER_NUCLEI = "nuclei"
os.makedirs(OUTPUT_FOLDER_SUBDO, exist_ok=True)
os.makedirs(OUTPUT_FOLDER_ACTIVE, exist_ok=True)
os.makedirs(OUTPUT_FOLDER_NUCLEI, exist_ok=True)


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

    __  __            __  _                
   / / / /_  ______  / /_(_)___  ____ _    
  / /_/ / / / / __ \/ __/ / __ \/ __ `/    
 / __  / /_/ / / / / /_/ / / / / /_/ /     
/_/ /_/\__,_/_/ /_/\__/_/_/ /_/\__, /      
                              /____/       
v0.3.1
                phims.tech
                novgrey.web.id
  """)
    print("📌 By PHIMS")
    print("🔗 GitHub: https://github.com/phims403")
    print("📷 Instagram: https://instagram.com/aier_phims\n")

def main():
    check_and_install_tools()
    update_tools()
    show_banner()

    target = input("Masukkan target (contoh: example.com): ").strip()
    if not target:
        print("[❌] Target tidak boleh kosong!")
        return

    subdomain_file = os.path.join(OUTPUT_FOLDER_SUBDO, f"{target}.txt")
    active_file = os.path.join(OUTPUT_FOLDER_ACTIVE, f"active_{target}.txt")
    nuclei_output = os.path.join(OUTPUT_FOLDER_NUCLEI, f"nuc_active_{target}.txt")





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
                  

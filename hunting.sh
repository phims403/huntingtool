#!/bin/bash

# Warna untuk output
GREEN="\e[32m"
RED="\e[31m"
YELLOW="\e[33m"
RESET="\e[0m"

# Tools yang diperlukan
TOOLS=(
    "github.com/projectdiscovery/subfinder/v2/cmd/subfinder"
    "github.com/projectdiscovery/httpx/cmd/httpx"
    "github.com/projectdiscovery/nuclei/v2/cmd/nuclei"
)

# Mengecek apakah Go sudah terinstall
if ! command -v go &> /dev/null; then
    echo -e "${RED}[❌] Go tidak ditemukan!${RESET} Install Go terlebih dahulu."
    exit 1
fi

# Fungsi untuk menginstall tools
install_tools() {
    for tool in "${TOOLS[@]}"; do
        tool_name=$(basename "$tool")
        if ! command -v "$tool_name" &> /dev/null; then
            echo -e "${YELLOW}[⚠️] ${tool_name} belum terinstall, menginstall...${RESET}"
            go install -v "$tool"@latest
            if [ $? -eq 0 ]; then
                echo -e "${GREEN}[✅] ${tool_name} berhasil diinstall.${RESET}"
            else
                echo -e "${RED}[❌] Gagal menginstall ${tool_name}.${RESET}"
            fi
        else
            echo -e "${GREEN}[✅] ${tool_name} sudah terinstall.${RESET}"
        fi
    done
}

# Fungsi untuk memperbarui tools
update_tools() {
    echo -e "${YELLOW}[🔄] Memperbarui semua tools...${RESET}"
    for tool in "${TOOLS[@]}"; do
        tool_name=$(basename "$tool")
        if command -v "$tool_name" &> /dev/null; then
            "$tool_name" -update &> /dev/null
        fi
    done
    nuclei -update-templates &> /dev/null
    echo -e "${GREEN}[✅] Semua tools telah diperbarui.${RESET}"
}

# Banner
banner() {
    clear
    echo -e "${GREEN}
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
    ${RESET}"
    echo -e "${YELLOW}📌 By PHIMS${RESET}"
    echo -e "${YELLOW}🔗 GitHub: https://github.com/username${RESET}"
    echo -e "${YELLOW}📷 Instagram: https://instagram.com/username\n${RESET}"
}

# Fungsi utama
main() {
    install_tools
    update_tools
    banner

    read -p "Masukkan target (contoh: example.com): " target
    if [[ -z "$target" ]]; then
        echo -e "${RED}[❌] Target tidak boleh kosong!${RESET}"
        exit 1
    fi

    subdomain_file="${target}.txt"
    active_file="active_${target}.txt"
    nuclei_output="nuc_active_${target}.txt"

    echo -e "${YELLOW}[🔍] Mencari subdomain...${RESET}"
    subfinder -d "$target" -o "$subdomain_file"

    echo -e "${YELLOW}[🌐] Mengecek subdomain yang aktif...${RESET}"
    httpx -l "$subdomain_file" -o "$active_file"

    echo -e "${YELLOW}[🚀] Menjalankan Nuclei scan...${RESET}"
    nuclei -l "$active_file" -severity low,medium,high,critical -o "$nuclei_output"

    echo -e "${GREEN}[✅] Semua proses selesai!${RESET}"
}

# Jalankan script utama
main

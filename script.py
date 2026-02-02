import os
import random
from datetime import datetime, timedelta

# --- DATA USER ---
email_github = "lfathhbusines@gmail.com"
nama_github  = "lfathh"
tahun_target = 2026
# -----------------

# List pesan commit biar terlihat seperti coding beneran
pesan_commit = [
    "fix typo in readme", "update logic", "refactor code", 
    "add new feature", "optimize performance", "bug fix", 
    "update dependencies", "clean up code", "wip", 
    "initial commit", "merge branch", "update styles"
]

def main():
    print(f"Mengatur Git user ke: {nama_github}...")
    os.system(f'git config user.email "{email_github}"')
    os.system(f'git config user.name "{nama_github}"')

    # Mulai dari 1 Jan tahun ini
    start_date = datetime(tahun_target, 1, 1)
    
    # BERHENTI DI HARI INI (Real time)
    end_date = datetime.now() 

    current_date = start_date
    delta = timedelta(days=1)

    print(f"Mengisi commit dari {start_date.date()} sampai {end_date.date()}...")

    total_commits = 0
    while current_date.date() <= end_date.date():
        # LOGIKA NATURAL:
        # 1. Jumlah commit acak 1-10 per hari (biar warna beda-beda)
        # 2. Kadang-kadang ada hari yang sangat sibuk (bonus commit)
        jumlah_commit = random.randint(1, 10)
        if random.random() < 0.1: # 10% peluang hari lembur
            jumlah_commit += 5
        
        print(f"Processing {current_date.date()}: {jumlah_commit} commits")

        for _ in range(jumlah_commit):
            # JAM NATURAL: Commit antara jam 09:00 pagi - 23:00 malam
            jam = random.randint(9, 23)
            menit = random.randint(0, 59)
            detik = random.randint(0, 59)
            
            waktu_commit = current_date.replace(hour=jam, minute=menit, second=detik)
            
            # Jangan commit jika waktunya melebihi waktu SEKARANG (untuk hari ini)
            if waktu_commit > datetime.now():
                continue

            date_str = waktu_commit.strftime('%Y-%m-%d %H:%M:%S')
            pesan = random.choice(pesan_commit)

            # Tulis file
            with open('contribution.txt', 'a') as f:
                f.write(f'{date_str} - {pesan}\n')
            
            # Git process
            os.system('git add contribution.txt')
            os.system(f'git commit -q --date="{date_str}" -m "{pesan}"')
            total_commits += 1
        
        current_date += delta

    print(f"\n✅ SELESAI! Total {total_commits} commit natural dibuat sampai hari ini.")
    print("Jalankan: git push -f origin main")

if __name__ == "__main__":
    main()


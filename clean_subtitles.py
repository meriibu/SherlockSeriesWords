
import os
import re

# Altyazı dosyalarının bulunduğu klasör
srt_folder = r"C:\Users\Lenovo\Downloads\sherlock.unaired.pilot.(2010).tv.s01.e00.eng.7cd"

# Temizlenmiş metni saklamak için bir dosya oluştur
output_file = "cleaned_transcript.txt"

# Tüm srt dosyalarını oku ve metni temizle
with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in os.listdir(srt_folder):
        if filename.endswith(".srt"):
            with open(os.path.join(srt_folder, filename), "r", encoding="utf-8") as infile:
                content = infile.read()

                # Zaman kodlarını ve gereksiz satırları sil
                cleaned_content = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', content)
                cleaned_content = re.sub(r'<[^>]+>', '', cleaned_content)  # HTML etiketleri varsa sil
                cleaned_content = re.sub(r'\d+\n', '', cleaned_content)  # Satır numaralarını sil
                cleaned_content = re.sub(r'\s+', ' ', cleaned_content)  # Gereksiz boşlukları sil

                outfile.write(cleaned_content + "\n")

print(f"Temizlenmiş metin {output_file} dosyasina yazildi.")

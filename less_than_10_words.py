from collections import Counter
import re

# Temizlenmiş metin dosyasını oku
with open("cleaned_transcript.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

# Kelimeleri metinden çıkar
words = re.findall(r'\b\w+\b', text)

# Kelime frekanslarını hesapla
word_count = Counter(words)

# 10 defadan az kullanılan kelimeleri bul
less_than_10 = [word for word, freq in word_count.items() if freq < 10]

# Az kullanılan kelimeleri bir dosyaya yaz
output_file = "less_than_10_words.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for word in less_than_10:
        file.write(word + "\n")

print(f"Az kullanılan kelimeler {output_file} dosyasına yazıldı.")

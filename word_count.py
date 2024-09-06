from collections import Counter
import re

# Temizlenmiş metin dosyasını oku
with open("cleaned_transcript.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

# Kelimeleri metinden çıkar
words = re.findall(r'\b\w+\b', text)

# Kelime frekanslarını hesapla
word_count = Counter(words)

# En sık kullanılan kelimeleri yazdır
most_common_words = word_count.most_common(100)  # İlk 100 kelimeyi al
for word, freq in most_common_words:
    print(f"{word}: {freq}")

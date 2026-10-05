# 03_jumlah_per_baris.py
# Pertemuan 06 - Nested Loop dan Akumulasi

print("=" * 40)
print("       JUMLAH PER BARIS PERKALIAN")
print("=" * 40)

for i in range(1, 5):
    total_baris = 0

    for j in range(1, 4):
        hasil = i * j
        total_baris += hasil

    print(f"Baris {i} : total = {total_baris}")

print("-" * 40)
print("Perhitungan selesai.")
print("=" * 40)
# 01_pasangan_indeks.py
# Pertemuan 06 - Nested Loop

print("=" * 35)
print("      DAFTAR PASANGAN INDEKS")
print("=" * 35)

jumlah_pasangan = 0

for i in range(1, 4):
    for j in range(1, 5):
        jumlah_pasangan += 1
        print(f"Pasangan ke-{jumlah_pasangan:02d} : (i={i}, j={j})")

print("-" * 35)
print(f"Total pasangan : {jumlah_pasangan}")
print("=" * 35)
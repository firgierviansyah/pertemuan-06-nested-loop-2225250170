# 02_pola_segitiga.py
# Pertemuan 06 - Nested Loop

print("=" * 35)
print("       POLA SEGITIGA BINTANG")
print("=" * 35)

n = int(input("Masukkan jumlah baris: "))

if n <= 0:
    print("Jumlah baris harus lebih dari 0.")
else:
    print("\nHasil pola:")

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

print("=" * 35)
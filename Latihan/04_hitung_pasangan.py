# 04_hitung_pasangan.py
# Pertemuan 06 - Nested Loop dan Pencacahan

print("=" * 40)
print("       HITUNG PASANGAN YANG VALID")
print("=" * 40)

n = int(input("Masukkan nilai n: "))

if n <= 0:
    print("Nilai n harus lebih dari 0.")
else:
    jumlah_pasangan = 0

    print(f"\nPasangan dengan i + j <= {n}:")

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i + j <= n:
                jumlah_pasangan += 1
                print(f"({i}, {j})", end=" ")

        print()

    print("-" * 40)
    print(f"Total pasangan valid : {jumlah_pasangan}")

print("=" * 40)
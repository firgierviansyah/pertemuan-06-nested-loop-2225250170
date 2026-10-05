# tabel_perkalian_dan_statistik.py
# Pertemuan 06 - Nested Loop, Akumulasi, dan Pencacahan

print("=" * 50)
print("       TABEL PERKALIAN DAN STATISTIK")
print("=" * 50)

# Validasi input
while True:
    n = int(input("Masukkan ukuran tabel (n): "))

    if n > 0:
        break

    print("Input tidak valid. n harus lebih dari 0.")

# Inisialisasi statistik keseluruhan
total_semua = 0
count_genap = 0

print("\nTabel Perkalian:")
print("-" * 50)

# Nested loop untuk membuat tabel
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j

        print(f"{hasil:4}", end="")

        total_baris += hasil
        total_semua += hasil

        if hasil % 2 == 0:
            count_genap += 1

    print(f"   | Total baris {i} = {total_baris}")

print("-" * 50)

# Statistik keseluruhan
print(f"Total semua hasil : {total_semua}")
print(f"Jumlah hasil genap: {count_genap}")

print("=" * 50)
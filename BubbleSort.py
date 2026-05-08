import os

# Fungsi untuk membersihkan terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def bubble_sort(data):
    n = len(data)
    count = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data, count


# ================= PROGRAM UTAMA =================
clear_screen()

# Identitas
print("=== PROGRAM BUBBLE SORT ===")
print("Nama : Indira Suci")   # ganti sesuai nama kamu
print("NIM  : 552010125006")    # ganti sesuai NIM kamu
print("-" * 30)

# Data
data = [5, 2, 9, 1, 5, 6]

# Proses sorting
hasil, langkah = bubble_sort(data.copy())

# Output
print("Data awal        :", data)
print("Hasil sorting    :", hasil)
print("Jumlah perbandingan:", langkah)

import os

# Fungsi untuk membersihkan terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def insertion_sort(data):
    count = 0

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            count += 1
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
    return data, count

# ================= PROGRAM UTAMA =================
clear_screen()

# Identitas
print("=== PROGRAM INSERTION SORT ===")
print("Nama : Indira Suci")   # ganti sesuai nama kamu
print("NIM  : 552010125006")    # ganti sesuai NIM kamu
print("-" * 30)

data = [5, 2, 9, 1, 5, 6]
hasil, langkah = insertion_sort(data.copy())

print(" hasil:", hasil)
print("jumlah perbandingan:", langkah)

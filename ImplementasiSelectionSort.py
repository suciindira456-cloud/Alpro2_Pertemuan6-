import os

# Fungsi untuk membersihkan terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def selection_sort(data):
    n = len(data)
    count = 0

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            count += 1
            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]
    return data, count


# ================= PROGRAM UTAMA =================
clear_screen()

# Identitas
print("=== PROGRAM SELECTION SORT ===")
print("Nama : Indira Suci")   # ganti sesuai nama kamu
print("NIM  : 552010125006")    # ganti sesuai NIM kamu
print("-" * 30)

data = [5, 2, 9, 1, 5, 6]
hasil, langkah = selection_sort(data.copy())

print(" hasil:", hasil)
print("jumlah perbandingan:", langkah)

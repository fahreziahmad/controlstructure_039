# Fungsi untuk mencetak angka ganjil hingga batas n yang diinput

def angka_ganjil():
    n = int(input("Masukkan batas n untuk angka ganjil: "))
    ganjil = [i for i in range(1, n + 1) if i % 2 != 0]
    print("Angka ganjil hingga", n, "adalah:", ganjil)

# Memanggil fungsi
angka_ganjil()
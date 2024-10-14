def fibonacci(n):
    a, b = 0, 1
    hasil = []
    while a < n:
        hasil.append(a)
        a, b = b, a + b
    return hasil

#memanggil fungsi dengan input dari pennguna
n = int(input("Masukkan batas n untuk seri Fibonacci: "))
print("seri Fibonacci hingga", n, "adalah:", fibonacci(n))
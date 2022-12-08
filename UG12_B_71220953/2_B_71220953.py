print("~~~ Selamat Datang di Kalkulator Sederhana ~~~")
choice = str(input("Masukkan operator matematika yang ingin Anda hitung: "))
if choice == "+":
    cho2=int(input("Mau penjumlahan berapa: "))
    cho3=int(input("Print berapa banyak: "))
    for i in range (cho2-2,cho3+1):
        print((cho2-2), "+", i, "=", (cho2-2)+cho2)
else:
    print("Maaf, Operator Matematika yang anda cari belum tersedia.")
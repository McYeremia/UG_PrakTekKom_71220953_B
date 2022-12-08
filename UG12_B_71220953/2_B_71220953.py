print("~~~ Selamat Datang di Kalkulator Sederhana ~~~")
choice = str(input("Masukkan operator matematika yang ingin Anda hitung: "))
if choice == "+":
    a = 1
    cho2=int(input("Mau penjumlahan berapa: "))
    cho3=int(input("Print berapa banyak: "))
    for i in range (cho2,0-1): 
        print(cho2,"+", a, "=", (cho2+a))
while yesno == "t":
    yesno = input("Apakah anda ingin menghitung lagi? (y/t): ")       
    print("Terima Kasih dan Sampai Jumpa Lagi!")
else:
    print("Maaf, Operator Matematika yang anda cari belum tersedia.")
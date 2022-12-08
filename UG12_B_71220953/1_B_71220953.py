x = int(input("Masukkan Angka: "))
print(" "*(x-1),"*")
for j in range ((x-1),1,-1):
    print(" "*(j-1),"**")
print("**"*x)
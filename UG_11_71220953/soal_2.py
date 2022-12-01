k = str(input("Masukkan kata: "))

def funPalindrome():
    if k == k[::-1]:
        print ("Yes")
        print ("Jika dibalik: ", k[::-1])
    else:
        print("No")
        print("Jika dibalik: ",k[::-1])
funPalindrome()

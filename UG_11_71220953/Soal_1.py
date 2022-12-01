print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

pilihan = int(input("Enter choice(1/2/3/4): "))
if pilihan == 1:
    def add():
        asatu = int(float(input("Enter first number: ")))
        adua = int(float(input("Enter second number: ")))
        tambah = float(asatu + adua)
        print(asatu,"+",adua ,"=", tambah)
    add()
elif pilihan == 2:
    def subtract():
        asatu = int(float(input("Enter first number: ")))
        adua = int(float(input("Enter second number: ")))
        kurang = float(asatu - adua)
        print(asatu,"-",adua ,"=", kurang)
    subtract()
elif pilihan == 3:
    def multiply():
        asatu = int(float(input("Enter first number: ")))
        adua = int(float(input("Enter second number: ")))
        kali = float(asatu * adua)
        print(asatu,"*",adua ,"=", kali)
    multiply()
elif pilihan == 4:
    def divide():
        asatu = int(float(input("Enter first number: ")))
        adua = int(float(input("Enter second number: ")))
        bagi = float(asatu / adua)
        print(asatu,"/",adua ,"=", bagi)
    divide()
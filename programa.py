
print("Interes compuesto")
c = float(input("Ingrese el capital: "))
n = 0
c_2 = c*2
mes = 0
while c < c_2:
    c = c + (c*0.05)
    n = n+1
    mes = mes + 1
    print(f"mes: {mes}    Capital: {c}")



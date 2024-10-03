def rana(n):
  if n == 0:
    return 0:
elif n == 1:
    return 1
else:
    return rana(n-1) + rana (-2)

def main():
    try:
      n = int(input("Ingrese un numero para calcular el enésimo numero de  Fibonnacci: "))
      if n < 0:
          print("por favor, ingrese un numero entero no negativo.")
      else:
          print(f"El enesimo numero de Fibonnacci para n={n} es {rana(n)}")
except ValueError:
    print("por favor, ingrese un numero entero valido.")
if __name__ == "__main__":
   main()

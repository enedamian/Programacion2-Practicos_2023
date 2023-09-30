"""
Realizar un programa que pida los tres lados de un triángulo e indique el tipo de
triángulo que es según sus lados: Equilátero (tres lados iguales), Isósceles (dos
lados iguales) o Escaleno (tres lados distintos).
"""
# posible solucion basica
print("Vamos a determinar el tipo de triángulo")
lado1 = float(input("Ingresá el primer lado: "))
lado2 = float(input("Ingresá el segundo lado: "))
lado3 = float(input("Ingresá el tercer lado: "))
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")

#-----------------------------------------------------------
# soluciones mejoradas:

# Mi solución:
def detTipoTriangulo(a, b, c):
    if a == b and b == c:
        return "Escaleno"
    elif a == b or b ==c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    try:    
        a = float(input("Ingresar longitud del lado a: "))
        b = float(input("Ingresar longitud del lado b: "))
        c = float(input("Ingresar longitud del lado c: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Los lados deben tener valores positivos.")
        elif a + b <= c or a + c <= b or b + c <= a:
            print("Estas longitudes no forman un triángulo.")
        else:
            tipo = detTipoTriangulo(a, b, c)
            print(f"El triángulo es {tipo}")

    except ValueError:
        print("Debe ingresar valores numéricos")
    
if __name__ == "___main__":
    main()
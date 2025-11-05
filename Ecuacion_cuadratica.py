#Calculo de ecuaciones de segundo grado

print("---Cálculo de raíces de una ecuación de segundo grado---")
while True:
    try:
        a=float(input("Ingresa el coeficiente a:"))
        b=float(input("Ingresa el coeficiente b:"))
        c=float(input("Ingresa el coeficiente c:"))
        break
    except (ValueError):
        print("Ingresa sólo números válidos")

def ecuacion(a,b,c):
    disc=(b*b-4*a*c)
    if a==0:
        x=-c/b
        print(f"La única solución de tu ecuación es {x}")
    elif disc<0:
        disc=-disc
        real=-b/(2*a)
        imag=(disc**0.5)/(2*a)
        if real==0:
            print(f"Las soluciones de tu ecuación son: {imag}i y -{imag}i")
        else:
            print(f"Las soluciones de tu ecuación son: {real}+{imag}i y {real}-{imag}i")
    
    else:
        x1=(-b+(disc)**0.5)/(2*a)
        x2=(-b-(disc)**0.5)/(2*a)
        print(f"Las soluciones de tu ecuación son: {x1} y {x2}")

ecuacion(a,b,c)

#Calculo de ecuaciones de segundo grado

print("---Cálculo de raíces de una ecuación de segundo grado---")
a=int(input("Ingresa el coeficiente a:"))
b=int(input("Ingresa el coeficiente b:"))
c=int(input("Ingresa el coeficiente c:"))

def ecuacion(a,b,c):
    disc=(b*b-4*a*c)
    if disc<0:
        imag=-disc
        x1=(-b+(imag)**0.5)/(2*a)
        x2=(-b-(imag)**0.5)/(2*a)
        print(f"Las raíces de tu ecuación son: {x1}i y {x2}i")
    
    else:
        x1=(-b+(disc)**0.5)/(2*a)
        x2=(-b-(disc)**0.5)/(2*a)
        print(f"Las raíces de tu ecuación son: {x1} y {x2}")

ecuacion(a,b,c)
"""
Reciba 3 notas del Usuario

calcule y muestre el promedio

40
45
50

Su promedio es: 45
"""

Nota1 = int(input("Ingresa Nota 1 >"))

Nota2 = int(input("Ingresa Nota 2 >"))

Nota3 = int(input("Ingresa Nota 3 >"))

suma = Nota1 + Nota2 + Nota3

promedio = suma / 3

"""
Los estudiantes pasan cuando el promedio es mayor o igual a 35
"""

if promedio >= 35:
    print ("Pasate la materia")
elif promedio >= 30:
    print ("Con una recuperacion pasas")
elif promedio >= 20:
    print ("Tu lo que vales es monda")
else:
    print("Pasaste la materia")  

print ("Tu promedio es..", promedio)
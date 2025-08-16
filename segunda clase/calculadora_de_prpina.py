"""
Me dio pereza copiar pq esta muy largo

pero es una calcualdora de propina0
"""

Total_Comida = int(input("Precio total de la comida >"))

if Total_Comida < 0:
    Total_Comida *= -1

Propina = float(input("Cuanta propina deseas pagar >"))

if Propina < 0:
    Propina *= -1

Personas = int(input("Con cuantas personas te vas a dividir la cuenta >"))

if Personas < 0:
    Personas *= -1
elif Personas == 0:
    Personas = 0

Resultado = (Total_Comida + ((Propina/100)*Total_Comida))/Personas

print(f"""
      Precio Total Comida : $ {Total_Comida}
      Porcentaje de propina : {Propina}%
      Personas para dividir la cuenta : {Personas}
      Cada uno debe pagar : ${Resultado}
      """)
#problema 1
print("hola mundo")

#Prolblema 2
nombre= input("Por favor ingrese su nombre: ")

if nombre.isalpha():
    print(f"Mucho gusto, {nombre}")

else:
     print("Ingrese un nombre real")

#Problema 3
edadBase=18

edadDeusuario=int(input("¿Cuantos años tienes?: "))

if edadDeusuario>=edadBase:
   print("Usted es mayor de edad")

else:
   print("usted tiene la edad de un fan de plin plin (es menor de edad)")

#Problema 4

numero= input("Ingrese un número que no sea decimal: ")

parteDecimal = float(numero)
parteEntera = int(parteDecimal)

comprobacion= parteDecimal%2

if parteDecimal == parteEntera:
   if comprobacion==1:
      print("Sú número es impar")
   else:
      print("Sú número es par")
else: 
   print("Su número es un decimal")   

#Problema 5
numero= input("Ingrese un número que no sea decimal: ")

parteDecimal = float(numero)
parteEntera = int(parteDecimal)

if parteDecimal == parteEntera:
   resultado=parteEntera*(parteEntera+1)//2
   print(f"El valor de la suma de 1 hasta su número ingresado es {resultado}")
else: 
   print("Su número es un decimal")  

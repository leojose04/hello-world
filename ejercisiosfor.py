#import time
#def ejercisio1 ():
    #palabra= str(input("por favor ingresar palabra"))
    #cantidad= int(input("ingrese la cantidad de veces que se repita la palabra"))
    #for i in range(cantidad):
        #print ("valor de la variable i :" , i+1)
        #time.sleep(0.5)
        #print(palabra)
    #return palabra
#ejercisio1()

#import time
#def ejercisio2 ():
    #palabra= int(input("cual es tu edad"))
    #for i in range(palabra):
        #print ("tienes :" , i+1 , "años")
        #time.sleep(2)    
    #return palabra
#ejercisio2()

import time
#def ejercisio3 ():
    #fechaN= int(input("cual es tu fecha de nacimiento"))
    #fechaA= int(input("cual es el año en la actualidad"))
    #rest= (fechaA-fechaN)
    #print ("tu edad es :" , rest , "años")
    #for i in range(rest):
        #print (i+1)
        #time.sleep(2)
    #return rest

#ejercisio3()

#def numeros_impares():
    #numero= int(input("ingrese el numero : "))
    #for i in range(1,numero, 2):
        #time.sleep (1)
        #print(i, end= ", \n")
        #if i == 15:
            #break

#numeros_impares()

#def reloj ():
    #timemax= int(input("ingrese el segundo de descanso"))
    #for i in range(1,60+1,1):
        #print (i, end=" , \n")
        #time.sleep(0.1)
        #if i == timemax:
            #print ("llego al segundo de descanso")
            #break
        #if i ==60:
            #print ("llego al minuto")
            
            

#reloj()

#def inver_compuesto():
    #Dinero = int(input("ingrese cuanta plata tienes en el banco"))
    #Interes = int(input("cual es el interes que tienes anualmente"))
    #Años = int(input("cuantos años"))
    #Valor_compuesto = Dinero * (1 + Interes / 100) ** Años
    #print("Tu plata en el banco al finalizar los años es: ", Valor_compuesto)
    #for i in range(Años):
    #    print(i, "años:", Dinero * (1 + Interes / 100) ** i)
    #    time.sleep(1)

#inver_compuesto()
import time
def triangulos():
    triangulo = int(input("ingrese la cantidad de filas"))
    for i in range(triangulo):
        print("" * (triangulo - i - 1) + "*" * (2 * i + 1))
        time.sleep(0.5)
#triangulos ()

def descubrir_contraeña():
    contraseña = "123456789"
    contraseña_ingresada = ""
    intento_ingresado = int(input("porfa ingrese la cantidad de intentos"))
    intento= 1
    while contraseña_ingresada != contraseña:
        contraseña_ingresada = str(input("ingrese su contraseña: "))
        if contraseña_ingresada != contraseña:
            print("Contraseña no coincide")    
        if contraseña_ingresada == contraseña:
            print("Contraseña correcta")
            break
        if intento == intento_ingresado:
            print("se llego a limite")
            break
        intento = intento + 1

#descubrir_contraeña()

def frases_contadas():
    frase = str(input("ingrese una frase: "))
    letra = str(input("ingrese la letra que quieres buscar"))
    contador = 0
    for i in frase:
        if i == letra:
            contador = contador + 1
    print("La letra", letra, "aparece", contador, "veces en la frase")
#frases_contadas()



import random
#def suma_dos_valores (sumando1, sumando2):
    #global resultado
    #resultado = sumando1 + sumando2
    #return resultado

#suma_dos_valores (4,5)
#print ("primera suma")
#print (resultado)
#suma_dos_valores (1,2)
#print (resultado)

#def calculadora_dos_valores (numero1, numero2, operador):
    #global resultado
    #if operador == ("suma"): #si el operador es 1 es suma
        #resultado = numero1 + numero2
        #return resultado
    #elif operador == ("resta"): #si el operador es 2 es resta
        #resultado = numero1 - numero2
        #return resultado
    #elif operador == ("multiplicacion"): #si el operador es 3 se multiplica
        #resultado = numero1 * numero2
        #return resultado
    #elif operador == ("division"): #si el operador es 4 se divide
        #resultado = numero1 / numero2
        #return resultado
    #else: #si el operador es otro numero
        #print ("el numero ingresado no es valido")
    #return resultado

#calculadora_dos_valores (1,2,"suma")
#print ("suma =",resultado)
#calculadora_dos_valores (10,5,"resta")
#print ("resta =", resultado)
#calculadora_dos_valores (10,5,"multicacion")
#print ("multiplicacion =", resultado)
#calculadora_dos_valores (10,4,"division")
#print ("division =" , resultado)
    
#def pitagoras (a,b):
   # global c
    #c=(a**2+b**2)**0.5
    #return c
#pitagoras = (3,4)
#print ("pitagoras",c)

#def despeje_x ():
    #global x
    #b=int(input("ingrese al valor de b"))
    #c=int(input("ingrese al valor de c"))
    #x=(c-b)/2
    #print ("el valor de x es :", x)
    #return x
#despeje_x()



#def compuerta_and ():
   # global resultado
    #m= bool (input("ingrese si  m es true o false"))
    #n= bool (input("ingrese si  n es true o false"))
    #b= bool (input("ingrese se  b es true o false"))
    #resultado = m and n and b
    #print ("el resultado es :", resultado)
    #return resultado

#compuerta_and ()

#def pitagoras_funcion_sumar ():
    #global result_pitagoras
    #a=int(input("ingrese el valor de a"))
    #b=int(input("ingrese el valor de b"))
    #a2= a**2 
    #b2= b**2
    #suma= suma_dos_valores (a2,b2)
    #result_pitagoras =suma**0.5
    #print ("el valor de pitagoras es :", result_pitagoras)
    #return result_pitagoras
   
#pitagoras_funcion_sumar()

#def contador_leras ():
    #global numerador
    #palabra = str(input("ingrese la palabra contar"))
    #letras = str(input("ingrese la letra a contador"))
    #numerador = palabra.count(letras)
    #x = len (palabra)
    #print ("el numero de veces que se repite la letra es :", numerador)
    #print ("el numero de caracteres en la palabra es :", x)
    #palabra = list(palabra)
    #print (palabra)


    #return numerador
#contador_leras()

def piedra_papel_tijera():
    
    opciones = ["piedra", "papel", "tijera"]
    jugador2 = random.choice(opciones)
    jugador = random.choice(opciones)
    if jugador == jugador2:
        resultado = "empate"
    elif (jugador == "piedra" and jugador2 == "tijera") or (jugador == "papel" and jugador2 == "piedra") or (jugador == "tijera" and jugador2 == "papel"):
        resultado = "gana jugador 1"
    else:
        resultado = "gana jugador 2"
    print("el jugador 1:", jugador)
    print("el jugador 2:", jugador2)
    print("El resultado :", resultado)
    return resultado

piedra_papel_tijera()



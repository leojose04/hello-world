import time
print("hola mundo \n") # esta linea imprime en consola la palabra hola mundo 
time.sleep(5)
print("segundo plano") 

print (type("hola")) # la funcion type me dice que tipo de dato esta en los parenctecis 
print (type(4))
print (type(5.5))
print ("pruebagitignore")
print ("-----------------------------------------------------------")
bool = True
print (bool)
print(type(bool))

numero = 5
texto = "hola"
suma= str (numero) + texto
print (suma)

bool1= True
bool2= False  

suma2 = bool1 and bool2
print (suma2)
a= False
b= False
c=False
d= True

resultdado = (((a and b) and c) or d)
print ("el resultado es :",resultdado) 
A=True
B=True
C=True
D=True
resultdado2= (A and B and C and D)
print (resultdado2)
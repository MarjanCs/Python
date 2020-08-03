def definir_matriz(cadena, matriz):
  cont = 0 #rastrear los indeces que se han ingresado en la lista
  lista = cadena.split(",")

  if len(lista) == (len(matriz)*len(matriz[0])):
    for i in range(len(matriz)):
      #se llena desde la ultima fila hasta la primera 
      j = len(matriz)-1
      while (j >= 0):
        matriz[i][j] = lista[cont]
        j = j-1
        cont = cont+1
  return matriz


def presentar_central(matriz):
  indice_central = len(matriz)//2
  central = matriz[indice_central][indice_central]
  return central

def imprimir_matriz(matriz):
  """
  Imprime una matriz de manera ordenada
  """
  for i in matriz:
    print(i)

def imprimir_menu():
  """
  Esta funcion imprime el menu
  """
  print("Que desea realizar en la matriz")
  print("1. Presentar el nro Central ")
  print("2. Presentar los nros en forma espiral desde el centro ")
  print("3. Multiplos del nro central")


print('Proyecto Final PYTHON')

n=int(input('Ingrese el tamano: '))
while(n%2==0) or n<3:
  print('Numero invalido')  

  n=int(input('Ingrese nuevamente el tamano: '))

print('Conociendo la matriz')
filas=n
columnas=n
matriz = [] 

a = str(input('Ingrese los valores separados por comas: '))
a = a.replace("(", "")
a = a.replace(")", "")
for i in range (filas): 
  matriz.append([])
  for j in range (columnas):
    matriz[i].append(0)

matriz = definir_matriz(cadena=a, matriz=matriz)
imprimir_matriz(matriz)

# Imprimimos el menu
imprimir_menu()

opcion=int(input("Respuesta -> "))

if opcion==1:
  matriz = presentar_central(matriz)
 

if opcion==2:
  pass
if opcion==3:
  pass





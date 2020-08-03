def definir_matriz(cadena,matriz):
  cont = 0 #rastrear los indeces que se han ingresado en la lista
  lista=cadena.split(",")
  print(lista)
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
  #se guarda los numeros de la diagonal princial en un array
  diagonalprin = []
 for i in range(0,filas):
  diagonalprin.append(matriz[i][i])

  #se guarda los numeros de la diagonal secundaria en un array
  diagonalsecu = []
 for i in range(0,columnas):
  diagonalsecu.append(matriz[i][(columnas-1)-i])

  #se encuentra el nuemero interseccion entreo los dos, osea el nro repetido el cual sera el centra
  a=diagonalprin[0]
 for i in range(0,len(diagonalsecu)):
  if diagonalsecu==a:
    a=diagonalsecu[i]
  b = diagonalprin.count(a)
  return diagonalprin[b]


print('Proyecto Final PYTHON')

n=int(input('Ingrese el tamaño: '))
while(n%2==0) or n<3:
  print('Numero invalido')  

  n=int(input('Ingrese nuevamente el tamano: '))

print('Conociendo la matriz')
filas=n
columnas=n
matriz = [] 

a=input('Ingrese los valores separados por comas: ')

for i in range (filas): 
  matriz.append([])
  for j in range (columnas):
    matriz[i].append(0)

matriz = definir_matriz(a,matriz)
print(matriz)

print('Que desea realizar en la matriz')
opcion=int(input('1. Presentar el nro Central '))
opcion=int(input('2. Presentar los nros en forma espiral desde el centro '))
opcion=int(input('3. Multiplos del nro central'))

if opcion==1:
  matriz = presentar_central(matriz)
  print (matriz)

if opcion==2:

if opcion==3:








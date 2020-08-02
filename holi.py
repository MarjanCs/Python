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


n=int(input('Ingrese el tamano: '))
while(n%2==0) orpy n<3:
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












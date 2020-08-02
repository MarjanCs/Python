n=int(input('Ingrese el tamano: '))
while(n%2==0) or n<3:
  print('Numero invalido')  

  n=int(input('Ingrese nuevamente el tamano: '))

print('Conociendo la matriz')
filas=n
columnas=n
matriz =[] 

for i in range (filas): 
  matriz.append([])
  for j in range (columnas):
    matriz[i].append(0)

for i in range(filas):
  for j in range(columnas):
    matriz[i][j]=int(input("Ingrese dato en fila {}, columna {} : ".format(i,j)))

for i in matriz:
  print(i)
print()

diagonalprin = []
for i in range(0,filas):
  diagonalprin.append(matriz[i][i])
print('principal')
print(diagonalprin)

print()
diagonalsecu = []
for i in range(0,columnas):
  diagonalsecu.append(matriz[i][(columnas-1)-i])
print('Secundaria')
print(diagonalsecu)

print()
a=diagonalprin[0]
for i in range(0,len(diagonalsecu)):
  if diagonalsecu==a:
    a=diagonalsecu[i]
b = diagonalprin.count(a)
print(diagonalprin[b])
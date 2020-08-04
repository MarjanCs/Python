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

def espiral(matriz):
  """
  Recorre la matriz en forma espiral desde el centro y retorna todos esos valores en una lista
  """
  result = []  # Lista resultado

  indice_central = indice_central = len(matriz) // 2
  
  # Coordenadas
  x = indice_central
  y = indice_central

  pasos = 1

  direcciones = ["derecha", "abajo", "izquierda", "arriba"]
  contador_direccion = 0



  # Agregamos el numero central ya a la lista antes de empezar
  result.append(matriz[x][y])
  print(result)
  iteraciones = 2 

  for k in range(len(matriz)*len(matriz)):

    for j in range(iteraciones):
      
      for i in range(pasos):
        direccion_actual = direcciones[contador_direccion]

        # Realizando el movimiento    
        if(direccion_actual == direcciones[0]):
          # Hacia la derecha
          x = x
          y = y + 1 
      
          if (len(matriz)) == y: # Verificamos si es que ya nos salimos de la matriz
            # Por aqui es la unica manera de salir
            return result

        elif direccion_actual == direcciones[1]:
          # Hacia abajo
          x = x + 1
          y = y 

        elif direccion_actual == direcciones[2]:
          # Hacia la izquierda
          x = x 
          y = y - 1

        elif direccion_actual == direcciones[3]:
          # Hacia arriba
          x = x - 1
          y = y 

        else:
          # Significa que direccion_actual tiene el valor de 4, y se ha salido de la lista, 
          #  por lo que debemos asumir que la direccion actual es 0, hacia la derecha
          contador_direccion = 0
          # Hacia la derecha
          x =  x + 1
          y = y 
      
          if (len(matriz)) == y: # Verificamos si es que ya nos salimos de la matriz
            # Por aqui es la unica manera de salir
            return result

        result.append(matriz[x][y])


      # Actualizamos la direccion actual para la siguiente iteracion
      contador_direccion = contador_direccion + 1
      if(contador_direccion == 4):
        contador_direccion = 0

    # La cantidad de pasos despues de dos iteraciones aumenta en uno
    pasos += 1

  return None


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
a = a.replace(" ", "")
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
  central = presentar_central(matriz)
  print(central)
 
if opcion==2:
  lista_resultado = espiral(matriz)
  print(lista_resultado)


if opcion==3:
  pass





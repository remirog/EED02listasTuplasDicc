colores=[] #Lista vacía
colores=['Rojo', 'Verde', 'Azul']
print("colores:", colores)
print("colores[0]:",colores[0])


colores[0]='Blanco'
print(f"colores: {colores}, colores[0]: {colores[0]}")
colores.append('Amarillo')
print("colores:", colores)

for i in colores:
    print(i)


print("colores:", colores)
#col=input("Dime un color:")
col='Azul'
try:
    pos= colores.index(col)
    print(f"Color indicado: {col}, posicion en lista: {pos}")
except Exception as e:
    print("El color indicado no se encuentra en la lista")

print("La ejecución del programa continua")




coloresMin=[ i.lower() for i in colores ]
print(coloresMin)
#color= input("Dime un color...")
color="VERde"
try: 
    
    pos=coloresMin.index(color.lower())
    print(f"{color} está en la lista en la posicion {pos}")
except Exception as e: 
    print(f"{color} no está en la lista")
    
colores.insert(1, "Gris")
print("colores:", colores)

try:
    colores.remove("Grises")

except:
    print(f"El color a borrar no está en la lista")

print("colores:", colores)

del colores[1] #Elimina el elemento en la posición 1 de la lista
print("colores:", colores)

listaNum1= [12, 4, 15, 6, 7, 23, 34, 66, 2, 1, 22]
print("listaNum1:", listaNum1)

listaNum1.sort() #Modifica la lista
print("listaNum1:", listaNum1)

listaNum1.sort(reverse=True)
print("listaNum1:", listaNum1)

listaNum2= [12, 4, 15, 6, 7, 23, 34, 66, 2, 1, 22]
print("listaNum2:", listaNum2)


#sorted es una función (no es un método como sort)
listaNum2Ord= sorted(listaNum2)  #listaNum2 queda si modificar
print("listaNum2:", listaNum2)
print("listaNum2Ord:", listaNum2Ord)

print("Num elementos listaNum1:", len(listaNum1))
listaNum3 = [1, 2] + [3, 4]
print("listaNum3:", listaNum3)

listaNum3.extend([5, 6])
print("listaNum3:", listaNum3)

listaNum3.extend(listaNum3)
print("listaNum3:", listaNum3)

#El elemento en la posición 6 no está incluido. Va de 1 a 5
listaNum4= listaNum3[1:6]
print("listaNum4:", listaNum4)

#Uso de rangos con salto
listaNum5Pares= listaNum3[1:len(listaNum3):2]
print("listaNum5Pares:", listaNum5Pares)

#En los rangos podemos omitir valores. Si omitimos el inicio
#el rango comenzará en el primero de la lista. Si omitimos el
#fin, el rango irá hasta el último elemento de la lista. Si omitimos
#el salto, se toma con salto el valor 1
print("Rango listaNum3", listaNum3[6::])

#Se pueden utilizar rangos negativos para recorrer la lista
print("Rango listaNum3", listaNum3[-1:-13:-1])

print("Rango listaNum3", listaNum3[-1::-1])

listaNum6= ['A', 'B', 'C']
listaNum7= [1, 2, 3]

#Podemos definir sublistas
listaNum8 = [listaNum6, listaNum7]
print("listaNum8:", listaNum8)

#Acceso a un elemento de una sublista
print("listaNum8[1][1]:", listaNum8[1][1])
listaNum9= ['X', 'Y', 'Z']

listaNum8.append(listaNum9)
print("listaNum8:", listaNum8)

listaNum8.extend(listaNum9)
print("listaNum8:", listaNum8)

#Las listas pueden tener elementos de distinto tipo
listaNum10=[125, 'A', 2.3, True, [1, 2, 3]]
print("listaNum10:", listaNum10)

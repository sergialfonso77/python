
c = -14
d = -14
print (c is d)
print(id(c))
print(id(d))

x = None

if x is None:
    print("x no tiene valor")

x = 12
if (x == 12):
    print("x es igual a doce")
elif (x == 13):
    print("Mala suerte, x es igual a 13")
else:
    print("x no es igual ni a 12 ni a 13")

x = 13
mensaje1 = "x es igual a 12"
mensaje2 = "x no es igual a 12"
print(mensaje1 if (x == 12) else mensaje2)

x = 0
while (x <= 10):
    print(x)
    if (x == 5):
        break
    x += 1


lista = [ 'las manzanas', 'las peras', 'las naranjas', 'los tomates' ]
for fruto in lista:
    print('Mis frutos preferido son %s' % fruto)



for index, palabra in enumerate(lista):
    print ("La palabra es:", palabra, "su posición en la frase es:", index)

num_lineas = 3
print(f"""Este texto
se representará 
en {num_lineas} líneas
""")

print('{:>10}'.format('test'))

texto = "&&&&Esto&&es$$una$$prueba&&&"
print(texto.replace("&"," ").replace("$", " ").strip().upper())

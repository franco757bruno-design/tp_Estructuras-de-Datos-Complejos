print("--- actividades 1, 2 y 3 ---")

precios_frutas = {
    'banana': 1200, 
    'anana': 2500, 
    'melon': 3000, 
    'uva': 1450
}
print(f"diccionario original: {precios_frutas}")

precios_frutas['naranja'] = 1200
precios_frutas['manzana'] = 1500
precios_frutas['pera'] = 2300

print(f"diccionario tras anadir (act 1): {precios_frutas}")

precios_frutas['banana'] = 1330
precios_frutas['manzana'] = 1700
precios_frutas['melon'] = 2800

print(f"diccionario tras actualizar (act 2): {precios_frutas}")

lista_frutas = list(precios_frutas.keys())

print(f"lista de frutas (act 3): {lista_frutas}")

# -----------------------------------------------------------------

print("\n--- actividad 4 ---")
contactos = {}

print("por favor, carga 5 contactos:")
for i in range(5):
    nombre = input(f"introduce el nombre del contacto {i+1}: ")
    numero = input(f"introduce el numero de {nombre}: ")
    contactos[nombre] = numero
    print(f"contacto '{nombre}' guardado.")

print("\n--- consulta de contactos ---")
nombre_consulta = input("que numero de contacto deseas consultar? introduce el nombre: ")

numero_encontrado = contactos.get(nombre_consulta, "el contacto no existe.")

print(f"resultado: {numero_encontrado}")

# -----------------------------------------------------------------

print("\n--- actividad 5 ---")
frase = input("introduce una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)
print(f"palabras unicas: {palabras_unicas}")

recuento_palabras = {}
for palabra in palabras:
    recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1

print(f"recuento de palabras: {recuento_palabras}")

# -----------------------------------------------------------------

print("\n--- actividad 6 ---")
alumnos = {}

for _ in range(3):
    nombre_alumno = input("introduce el nombre del alumno: ")
    
    try:
        nota1 = float(input(f"introduce la nota 1 de {nombre_alumno}: "))
        nota2 = float(input(f"introduce la nota 2 de {nombre_alumno}: "))
        nota3 = float(input(f"introduce la nota 3 de {nombre_alumno}: "))
        
        alumnos[nombre_alumno] = (nota1, nota2, nota3)
    except valueerror:
        print("error: introduce solo numeros para las notas.")
        alumnos[nombre_alumno] = (0, 0, 0)

print("\n--- promedios de alumnos ---")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"el promedio de {nombre} (notas: {notas}) es: {promedio:.2f}")

# -----------------------------------------------------------------

print("\n--- actividad 7 ---")
parcial_1 = {'a101', 'a102', 'a105', 'b201', 'b205'}
parcial_2 = {'a101', 'b201', 'b208', 'c301', 'a105'}

print(f"aprobaron parcial 1: {parcial_1}")
print(f"aprobaron parcial 2: {parcial_2}")

aprobaron_ambos = parcial_1.intersection(parcial_2)
print(f"estudiantes que aprobaron ambos parciales: {aprobaron_ambos}")

aprobaron_solo_uno = parcial_1.symmetric_difference(parcial_2)
print(f"estudiantes que aprobaron solo uno de los parciales: {aprobaron_solo_uno}")

total_aprobados = parcial_1.union(parcial_2)
print(f"lista total de estudiantes que aprobaron (al menos uno): {total_aprobados}")

# -----------------------------------------------------------------

print("\n--- actividad 8 ---")
stock_productos = {
    'tornillos': 1000,
    'tuercas': 800,
    'arandelas': 1500
}

while True:
    print("\n--- gestion de stock ---")
    print("1: consultar stock")
    print("2: agregar stock / nuevo producto")
    print("3: salir")
    opcion = input("elige una opcion: ")

    if opcion == '1':
        producto = input("introduce el nombre del producto a consultar: ").lower()
        cantidad = stock_productos.get(producto, "producto no encontrado")
        print(f"stock de '{producto}': {cantidad}")
        
    elif opcion == '2':
        producto = input("introduce el nombre del producto: ").lower()
        try:
            unidades = int(input(f"introduce la cantidad de '{producto}' a agregar: "))
            
            if producto in stock_productos:
                stock_productos[producto] += unidades
                print(f"stock de '{producto}' actualizado. nuevo total: {stock_productos[producto]}")
            else:
                stock_productos[producto] = unidades
                print(f"producto '{producto}' nuevo agregado con stock {unidades}.")
                
        except valueerror:
            print("error: introduce una cantidad numerica valida.")

    elif opcion == '3':
        print("saliendo del gestor de stock.")
        break
        
    else:
        print("opcion no valida. intentalo de nuevo.")

print(f"stock final: {stock_productos}")

# -----------------------------------------------------------------

print("\n--- actividad 9 ---")
agenda = {
    ("lunes", "10:00"): "reunion de equipo",
    ("martes", "15:00"): "clase de ingles",
    ("miercoles", "09:00"): "presentacion a cliente",
    ("viernes", "18:00"): "entrega tp"
}

print("--- consultar agenda ---")
dia_consulta = input("introduce el dia (ej: lunes): ").lower()
hora_consulta = input("introduce la hora (ej: 10:00): ")

clave_agenda = (dia_consulta, hora_consulta)

evento = agenda.get(clave_agenda, "no hay eventos programados para ese dia y hora.")

print(f"evento: {evento}")

# -----------------------------------------------------------------

print("\n--- actividad 10 ---")
paises_a_capitales = {
    "argentina": "buenos aires",
    "chile": "santiago",
    "brasil": "brasilia",
    "uruguay": "montevideo",
    "peru": "lima"
}

print(f"diccionario original: {paises_a_capitales}")

capitales_a_paises = {}

for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais

print(f"diccionario invertido: {capitales_a_paises}")
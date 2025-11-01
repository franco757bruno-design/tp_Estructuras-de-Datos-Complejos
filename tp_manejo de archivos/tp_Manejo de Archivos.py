nombre_archivo = "productos.txt"

print("--- actividad 1: creando archivo inicial ---")
try:
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write("lapicera,120.5,30\n")
        f.write("cuaderno,250.0,50\n")
        f.write("regla,80.75,20\n")
    print(f"archivo '{nombre_archivo}' creado con exito.")
except ioerror as e:
    print(f"error al crear el archivo: {e}")

# -----------------------------------------------------------------

print("\n--- actividad 4: leyendo archivo y cargando a memoria ---")
productos = []
try:
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            linea_limpia = linea.strip()
            if linea_limpia:
                
                datos = linea_limpia.split(",")
                
                try:
                    nombre = datos[0]
                    precio = float(datos[1])
                    cantidad = int(datos[2])
                    
                    producto_dic = {
                        'nombre': nombre,
                        'precio': precio,
                        'cantidad': cantidad
                    }
                    
                    productos.append(producto_dic)
                    
                except (indexerror, valueerror) as e:
                    print(f"advertencia: omitiendo linea mal formada: '{linea_limpia}' ({e})")
                    
    print(f"productos cargados en memoria: {len(productos)} items.")

except filenotfounderror:
    print(f"error: el archivo '{nombre_archivo}' no existe.")
except ioerror as e:
    print(f"error al leer el archivo: {e}")

# -----------------------------------------------------------------

print("\n--- actividad 2: mostrando productos desde la lista ---")
if not productos:
    print("no hay productos para mostrar.")
else:
    for p in productos:
        print(f"producto: {p['nombre']} | precio: ${p['precio']} | cantidad: {p['cantidad']}")

# -----------------------------------------------------------------

print("\n--- actividad 3: agregar producto nuevo (a la memoria) ---")
try:
    nombre_nuevo = input("ingrese nombre del nuevo producto: ")
    precio_nuevo = float(input(f"ingrese precio de {nombre_nuevo}: "))
    cantidad_nueva = int(input(f"ingrese cantidad de {nombre_nuevo}: "))
    
    nuevo_dic = {
        'nombre': nombre_nuevo,
        'precio': precio_nuevo,
        'cantidad': cantidad_nueva
    }
    
    productos.append(nuevo_dic)
    print(f"producto '{nombre_nuevo}' agregado a la lista en memoria.")
    
except valueerror:
    print("error: precio y cantidad deben ser numeros. producto no agregado.")

# -----------------------------------------------------------------

print("\n--- actividad 5: buscar producto por nombre ---")
if not productos:
    print("la lista de productos esta vacia, no se puede buscar.")
else:
    nombre_buscado = input("ingrese el nombre del producto a buscar: ")
    encontrado = false
    
    for p in productos:
        if p['nombre'].lower() == nombre_buscado.lower():
            print("producto encontrado:")
            print(f"  nombre: {p['nombre']}")
            print(f"  precio: ${p['precio']}")
            print(f"  cantidad: {p['cantidad']}")
            encontrado = true
            break
            
    if not encontrado:
        print(f"error: producto '{nombre_buscado}' no encontrado.")

# -----------------------------------------------------------------

print("\n--- actividad 6: guardando lista actualizada en el archivo ---")
try:
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            f.write(linea)
    print(f"archivo '{nombre_archivo}' actualizado con exito.")
except ioerror as e:
    print(f"error al guardar el archivo: {e}")

# -----------------------------------------------------------------

print("\n--- verificacion final: contenido del archivo guardado ---")
try:
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        print(f.read())
except ioerror as e:
    print(f"no se pudo leer el archivo para verificar: {e}")
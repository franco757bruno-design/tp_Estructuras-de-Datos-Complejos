def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    num_usuario = int(input("ingrese un numero para calcular factoriales: "))
    
    print(f"--- factoriales desde 1 hasta {num_usuario} ---")
    
    if num_usuario < 1:
        print("por favor, ingrese un numero entero positivo.")
    else:
        for i in range(1, num_usuario + 1):
            print(f"factorial de {i} = {factorial(i)}")

except ValueError:
    print("error: debe ingresar un numero entero.")

    #------------------------------------------------------------

    def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    pos_usuario = int(input("ingrese una posicion para la serie de fibonacci: "))
    
    if pos_usuario < 0:
        print("error: ingrese un numero positivo.")
    else:
        print(f"--- serie de fibonacci hasta la posicion {pos_usuario} ---")
        for i in range(pos_usuario + 1):
            print(fibonacci(i), end=" ")
        print() 

except ValueError:
    print("error: debe ingresar un numero entero.")

    #------------------------------------------------------------------

    def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

try:
    base_usuario = float(input("ingrese el numero base: "))
    exp_usuario = int(input("ingrese el exponente (entero): "))

    if exp_usuario < 0:
        print("este ejemplo solo funciona con exponentes positivos o cero.")
    else:
        resultado = potencia(base_usuario, exp_usuario)
        print(f"{base_usuario} elevado a {exp_usuario} = {resultado}")

except ValueError:
    print("error: ingrese numeros validos.")

    #----------------------------------------------------------------------

    def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

try:
    num_decimal = int(input("ingrese un numero decimal positivo: "))
    
    if num_decimal < 0:
        print("error: ingrese un numero positivo o cero.")
    else:
        resultado_binario = decimal_a_binario(num_decimal)
        print(f"el numero {num_decimal} en binario es: {resultado_binario}")

except ValueError:
    print("error: debe ingresar un numero entero.")

    #----------------------------------------------------------------------

    def es_palindromo(palabra):
    if len(palabra) < 2:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1:-1])

palabra_usuario = input("ingrese una palabra (sin espacios, tildes o mayusculas): ").lower()

if es_palindromo(palabra_usuario):
    print(f"'{palabra_usuario}' si es un palindromo.")
else:
    print(f"'{palabra_usuario}' no es un palindromo.")

    #---------------------------------------------------------------------------------

    def suma_digitos(n):
    if n < 10:
        return n
    
    return (n % 10) + suma_digitos(n // 10)

try:
    num_entero = int(input("ingrese un numero entero positivo: "))
    
    if num_entero < 0:
        print("error: ingrese un numero positivo.")
    else:
        resultado_suma = suma_digitos(num_entero)
        print(f"la suma de los digitos de {num_entero} es: {resultado_suma}")

except ValueError:
    print("error: debe ingresar un numero entero.")

    #-------------------------------------------------------------

    def contar_bloques(n):
    if n == 1:
        return 1
    
    return n + contar_bloques(n - 1)

try:
    nivel_base = int(input("ingrese el numero de bloques en el nivel mas bajo (n): "))
    
    if nivel_base < 1:
        print("error: el nivel base debe tener al menos 1 bloque.")
    else:
        total = contar_bloques(nivel_base)
        print(f"una piramide con {nivel_base} bloques en la base necesita un total de {total} bloques.")

except ValueError:
    print("error: debe ingresar un numero entero.")

    #------------------------------------------------------------

    def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    
    conteo_parcial = 0
    if (numero % 10) == digito:
        conteo_parcial = 1
        
    return conteo_parcial + contar_digito(numero // 10, digito)

try:
    num_entero = abs(int(input("ingrese un numero entero: ")))
    digito_buscado = int(input("ingrese el digito (0-9) que desea contar: "))
    
    if not (0 <= digito_buscado <= 9):
        print("error: el digito a buscar debe estar entre 0 y 9.")
    else:
        if num_entero == 0:
            conteo = 1 if digito_buscado == 0 else 0
        else:
            conteo = contar_digito(num_entero, digito_buscado)
            
        print(f"el digito {digito_buscado} aparece {conteo} veces en el numero {num_entero}.")

except ValueError:
    print("error: debe ingresar numeros enteros.")

    #-------------------------------------------------------

    
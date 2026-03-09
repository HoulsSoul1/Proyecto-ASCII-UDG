import os
import time

CARPETA_DATOS = "datos/"
galeria_guardada = []

if not os.path.exists(CARPETA_DATOS):
    os.makedirs(CARPETA_DATOS)

# ==========================================
# FUNCIONES DE FIGURAS 
# ==========================================

def submenu_patrones():
    print("\tMENÚ DE PATRONES")
    print("1. --- Triangulo")
    print("2. --- Cuadrado")
    print("3. --- Piramide")
    print("4. --- Volver al menu principal")
    
    opcion1 = int(input("Elige un patron: "))
    
    if opcion1 == 1:
        altura = int(input("Ingresa la altura del triangulo: "))
        triangulo = dibujo_triangulo(altura)
        print("\n" + triangulo)
        return f"Triangulo_{altura}", triangulo
    
    elif opcion1 == 2:
        lado = int(input("Ingrese el lado del cuadrado: "))
        cuadrado = dibujar_cuadrado(lado)
        print("\n" + cuadrado)
        return f"Cuadrado_{lado}", cuadrado
    
    elif opcion1 == 3:
        p = int(input("Ingresa la altura de la piramide: "))
        piramide = dibujar_piramide(p)
        print("\n" + piramide)
        return f"Piramide_{p}", piramide
    
    elif opcion1 == 4:
        return "", ""
    
    else: 
        print("Opcion no valida")
        return "", ""

def dibujo_triangulo(altura):
    resultado = ""
    for i in range(1, altura + 1):
        resultado += ("*" * i) + "\n" 
    return resultado

def dibujar_cuadrado(lado):
    resultado = ""
    for fila in range(lado):
        for columna in range(lado):
            if fila == 0 or fila == lado - 1 or columna == 0 or columna == lado - 1:
                resultado += "* "
            else:
                resultado += "  " 
        resultado += "\n" 
    return resultado

def dibujar_piramide(altura):
    resultado = ""
    for i in range(altura):
        espacios = " " * (altura - i - 1)
        estrellas = "*" * (2 * i + 1)
        resultado += espacios + estrellas + "\n"
    return resultado

## Este apartado de funciones se encarga de generar las figuras y un submenu 
## submenu_patrones(): Es la pantalla interactiva donde eliges qué figura quieres. Te pide las medidas (como la altura o el lado) para formar la figura
## dibujo_triangulo(altura): Usa un ciclo para imprimir líneas. En la línea 1 imprime un asterisco, en la 2 imprime dos, y así sucesivamente.
## dibujar_cuadrado(lado): Usa dos ciclos anidados (uno dentro de otro) para revisar filas y columnas.
## dibujar_piramide(altura): Dibuja una pirámide centrada calculando cuántos espacios en blanco debe dejar a la izquierda antes de empezar a imprimir los asteriscos en cada nivel.


#========================
# TEXTO ARTÍSTICO 
#========================

def submeno_artistico():
    print("\n ---- MENU ARTISTICO----")
    print("1. --- Marco")
    print("2. --- Banner")
    print("3. --- Tabla multiplicar")
    print("4. --- Volver al menú principal")
    
    opcion2 = int(input("Elige un numero: "))
    
    if opcion2 == 1:
        txt = input("Ingresa tu nombre: ")
        arte_actual = baner(txt)
        print("\n" + arte_actual)
        return f"Banner_{txt}", arte_actual
        
    elif opcion2 == 2:
        txt = input("Ingresa el texto: ")
        estilo = int(input("Elige estilo (1 para '~', 2 para '='): "))
        arte_actual = marco(txt, estilo)
        print("\n" + arte_actual)
        return f"Marco_{txt}", arte_actual
        
    elif opcion2 == 3:
        num = int(input("¿De qué número quieres la tabla?: "))
        arte_actual = tabla(num)
        print("\n" + arte_actual)
        return f"Tabla_{num}", arte_actual
        
    elif opcion2 == 4:
        return "", ""
        
    else: 
        print("Opcion no valida")
        return "", ""

def baner(texto):
    ancho = len(texto) + 4
    borde = "*" * ancho
    return borde + "\n* " + texto + " *\n" + borde + "\n"

def marco(texto, estilo):
    resultado = ""
    ancho = len(texto) + 8
    
    if estilo == 1:
        caracter = "~"
    else:
        caracter = "="
        
    borde = caracter * ancho
    resultado += borde + "\n"
    resultado += caracter + "   " + texto + "   " + caracter + "\n"
    resultado += borde + "\n"
    return resultado

def tabla(numero):
    resultado = baner(f"Tabla del {numero}")
    resultado += "Multiplicador\tResultado\n" 
    resultado += "-" * 25 + "\n"
    
    for i in range(1, 11):
        resultado += f"{numero} x {i}\t\t= {numero * i}\n"
    return resultado

## En estas funciones se hace lo mismo se crea un submenu para funciones artisticas y las funciones que va a ejecutar
## submeno_artistico(): Es el menú donde eliges si quieres un banner, un marco o una tabla. Toma los datos que escribes y te devuelve el arte generado.
## baner(texto): Calcula cuántas letras tiene tu texto y crea un borde superior e inferior de asteriscos
## marco(texto, estilo):Similar al banner, pero te permite elegir con qué símbolo quieres decorar los bordes (~ o =).
## tabla(numero): Crea una tabla de multiplicar clásica (del 1 al 10) usando un ciclo for, y la adorna poniéndole un título usando la función baner.

#==========================
#ANIMACIONES
#==========================

def submenu_animaciones():
    print("\n--- ANIMACIONES ---")
    print("1. --- Barra de Progreso")
    print("2. --- Texto en Movimiento")
    print("3. --- Volver al menu principal")
    
    opcion3 = int(input("Elige una opcion: "))
    
    if opcion3 == 1:
        barra_progreso()
    
    elif opcion3 == 2:
        texto_a_animar = input("Ingresa el texto a animar: ")
        animar_texto(texto_a_animar) 
    
    elif opcion3 == 3: 
        return 
    
    else:
        print("Opcion no valida numero (1-3)")

def barra_progreso():
    print("\nGenerando arte...")
    for i in range(0, 101, 10): 
        barra = "█" * (i // 10)
        espacios = "-" * (10 - (i // 10))
        print(f"\r[{barra}{espacios}] {i}%", end="")
        time.sleep(0.3)
    print("\n¡Completado!\n")

def animar_texto(texto):
    print("\nAnimación (terminará sola en unos segundos)...")
    for i in range(15):
        espacios = " " * i
        print(f"\r{espacios}{texto}", end="")
        time.sleep(0.2)
    print("\n") 


## Hace lo mismo que en los otras funciones crea un submenu y crea los diseños en este caso animados
## submenu_animaciones(): El menú de selección para las animaciones.
## barra_progreso(): Crea una falsa barra de carga, el carácter \r (retorno de carro), que hace que la consola borre la línea actual y escriba la nueva encima. Combinado con pausas de 0.3 segundos (time.sleep), da la ilusión de que la barra se está llenando.
## animar_texto(texto): Usa el mismo truco del \r y las pausas de tiempo, pero en lugar de dibujar una barra, va agregando espacios en blanco a la izquierda de tu texto. Esto hace que parezca que las letras se deslizan hacia la derecha


#=======================================
# FUNCIONES COMPLEMENTARIAS
#=======================================
    
    archivos = os.listdir(CARPETA_DATOS)
    for archivo in archivos:
        if archivo.endswith(".txt"):
            with open(CARPETA_DATOS + archivo, "r", encoding="utf-8") as f:
                # Evitar cargar duplicados verificando si ya existe en la lista
                nombres_existentes = [item['nombre'] for item in galeria_guardada]
                nombre_archivo = archivo.replace(".txt", "")
                
                if nombre_archivo not in nombres_existentes:
                    galeria_guardada.append({
                        "nombre": nombre_archivo,
                        "arte": f.read()
                    })
    if galeria_guardada:
        print(f"\n[!] Cargado exitosamente {len(galeria_guardada)} elementos de la galeria.")

def agregar_a_galeria(nombre, arte):
    galeria_guardada.append({"nombre": nombre, "arte": arte})
    print(f"\n¡'{nombre}' se agregó a la lista de tu galería actual!")

def exportar_arte(nombre, arte):
    ruta = CARPETA_DATOS + nombre + ".txt"
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(arte)
    print(f"¡Arte guardado físicamente en: {ruta}!")

def nombres_del_equipo():
    print("Axel Jeydan , Jose Nicolas, Francia Amayrany")

## Estas funciones se encargan de la memoria y al gestion de archivos
## carga_galeria(): Lee la carpeta datos/ buscando archivos .txt. Si encuentra dibujos guardados de sesiones anteriores, los carga en la lista del programa.
## agregar_a_galeria(nombre, arte): Toma el dibujo que acabas de hacer y lo guarda temporalmente en una lista (galeria_guardada) en la memoria RAM del programa.
## exportar_arte(nombre, arte): Toma el dibujo y crea un archivo de texto real y físico (un .txt) dentro de la carpeta datos/ para que lo guardes para siempre.
    
#================================
#MENU PRINCIPAL 
#================================

def mostrar_menu():
    print("\n ----MENÚ PRINCIPAL----")
    print("1. --- Patrones geometricos")
    print("2. --- Texto artistico")
    print("3. --- Animacion")
    print("4. --- Ver galeria")
    print("5. --- Limpiar galeria")
    print("6. --- Exportar a .txt")
    print("7. --- Salir del programa")

def iniciando_programa():
    arte_temporal = ""
    nombre_temporal = ""
    
    # Cargar archivos existentes al iniciar
    carga_galeria()
    
    while True: 
        mostrar_menu()
        
        opcion = int(input("\nElige un numero (1-7): "))
        
        if opcion == 1:
            nombre_temporal, arte_temporal = submenu_patrones()
            if arte_temporal != "":
                agregar_a_galeria(nombre_temporal, arte_temporal)
            1
        elif opcion == 2:
            nombre_temporal, arte_temporal = submeno_artistico()
            if arte_temporal != "":
                agregar_a_galeria(nombre_temporal, arte_temporal)
        
        elif opcion == 3:
            submenu_animaciones()
            
        elif opcion == 4:
            # Imprimir la galería almacenada
            if not galeria_guardada:
                print("\nLa galería está vacía.")
            else:
                for item in galeria_guardada:
                    print(f"\n--- {item['nombre']} ---")
                    print(item['arte'])
            
        elif opcion == 5:
            galeria_guardada.clear()
            print("\n¡La lista de la galería ha sido limpiada!")
            
        elif opcion == 6:
            if arte_temporal != "":
                exportar_arte(nombre_temporal, arte_temporal)
            else:
                print("\n❌ Primero debes crear un patrón o texto artístico.")
            
        elif opcion == 7:
            print("\n" + "="*60)
            print("Gracias por estar aqui, hasta pronto👋")
            nombres_del_equipo()
            break 
            
        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-7.")

if __name__ == "__main__":
    iniciando_programa()

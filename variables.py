# --- Paso 1: variblaes basicas ---
nombre = "Mateo"        #str (texto)
edad = 16                #int (numero entero)
altura = 1.68             #float (numero decimal)
es_estudiante = True      #bool (verdadero/falso)

# --- Paso 2: mostrarlas ---
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?:", es_estudiante)

# --- Paso 3: pedirle un dato al usuario ---
ciudad = input("¿En que ciudad vives? ")
print("Vives en ", ciudad)

# --- Paso 4: operar con numeros ---
edad_en_5_años = edad + 5
print("En 5 años tendras:", edad_en_5_años, "años")

# --- Paso 5: el error clasico de tipos (a proposito) ---
# Descomenta la siguiente linea y ejecuta de nuevo:
#mensaje = "Tengo " + edad + " años"
# --- Paso 1: aritmeticos ---
a = 17
b = 5

print("sumar:", a + b)
print("Resta:", a - b)
print("Multiplicacion:", a * b)
print("Division normal:", a / b)
print("Division enteral:", a //b)
print("Residuo (modulo):", a % b)

# --- Paso 2: comparacion ---
edad = 16
print("¿Edad mayor a 18?:", edad > 18)
print("¿Edad igual a 16?:", edad == 16)
print("¿Edad distinta de 16?:", edad != 16)

# --- Paso 3: logicos combinando condiciones ---
tiene_carnet = True
tiene_cita = False

puede_entrar_and = tiene_carnet and tiene_cita
puede_entrar_or = tiene_carnet or tiene_cita

print("¿Puede entrar (carnet Y cita)?:", puede_entrar_and)
print("¿Puede entrar (carnet O cita)?_", puede_entrar_or)

# --- Paso 4: el error clasico de = vs == (a propositivo) ---
# Descomenta la siguiente linea y ejecuta de nuevo:
# if edad = 16
#    print:("tiene 16")
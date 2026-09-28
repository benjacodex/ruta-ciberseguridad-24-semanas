# --- Paso 1: if/elif/else basico ---
edad = int(input("¿Cuantos años tienes?"))

if edad < 13:
    print("Boleto de niño")
elif edad < 18:
    print("Boleto de adolescente")
else:
    print("Boleto de adulto")
    
# --- Paso 2: condicion simple con else ---
saldo = 50
retiro =80

if retiro > saldo:
    print( "Fondos insuficientes")
else:
    saldo = saldo - retiro
    print("Retiro exitoso. Saldo restante:", saldo)
    
# --- Paso 3: el error clasico de indentacion (a proposito) --- 
# Descomenta este bloque y ejecuta de nuevo
# if edad > 0:
# print("Edad valida")                   
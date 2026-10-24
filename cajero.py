# Nombre del estudiante: Mariangel Marin Chinchilla 
# Contexto seleccionado: Cajero automático
# Descripción: permite varios retiros consecutivos sobre un saldo inicial
# hasta que el usuario decida salir o se agote el saldo.

# --- Constantes ---
SALDO_INICIAL = 250000
RETIRO_MINIMO = 5000
RETIRO_MAXIMO = 100000

# --- Inicialización ---
saldo = SALDO_INICIAL
retiros_exitosos = 0
respuesta = input("¿Desea realizar un retiro? (s/n): ").lower()

# --- Ciclo principal ---
while respuesta == "s" and saldo > 0:
    monto = int(input("Ingrese el monto a retirar (₡): "))

    if monto < RETIRO_MINIMO or monto > RETIRO_MAXIMO:
        print(f"Retiro no realizado: el monto debe estar entre ₡{RETIRO_MINIMO} y ₡{RETIRO_MAXIMO}.")
    elif monto > saldo:
        print("Retiro no realizado: fondos insuficientes.")
    else:
        saldo = saldo - monto
        retiros_exitosos = retiros_exitosos + 1
        print(f"Retiro realizado por ₡{monto}.")

    print(f"Saldo actual: ₡{saldo}")

    if saldo > 0:
        respuesta = input("¿Desea realizar otro retiro? (s/n): ").lower()

# --- Salida final ---
print("\n----------- Resumen -----------")
print(f"Saldo restante: ₡{saldo}")
print(f"Retiros exitosos: {retiros_exitosos}")
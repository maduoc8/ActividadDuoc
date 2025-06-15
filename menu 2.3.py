import random  # Para los valores aleatorios

# Diccionario para almacenar afiliados
afiliados = {}

# Ciclo principal del menú
while True:
    print("\n***** ISAPRE VIDA Y SALUD *****")
    print("1) Grabar afiliado")
    print("2) Buscar afiliado")
    print("3) Imprimir certificados")
    print("4) Salir")

    opcion = input("Ingrese una opción: ")

    # Opción 1: Grabar
    if opcion == "1":
        try:
            rut = input("Ingrese Rut: ").strip()
            if rut == "":
                print("El Rut no puede estar vacío.")
                continue
            if rut in afiliados:
                print("Este Rut ya está registrado.")
                continue

            nombre = input("Ingrese Nombre: ").strip()
            apellido = input("Ingrese Apellido Paterno: ").strip()

            edad = int(input("Ingrese Edad: "))
            if edad <= 18:
                print("La edad debe ser mayor a 18 años.")
                continue

            estado_civil = input("Ingrese Estado Civil (C=Casado, S=Soltero, V=Viudo): ").strip().upper()
            if estado_civil not in ["C", "S", "V"]:
                print("Estado Civil inválido. Solo C, S o V.")
                continue

            genero = input("Ingrese Género: ").strip()
            fecha = input("Ingrese Fecha de Afiliación (dd/mm/aaaa): ").strip()

            # Guardar en el diccionario
            afiliados[rut] = {
                "Nombre": nombre,
                "Apellido": apellido,
                "Edad": edad,
                "Estado Civil": estado_civil,
                "Género": genero,
                "Fecha": fecha
            }
            print(f"Afiliado con Rut {rut} registrado correctamente.")

        except ValueError:
            print("Error en los datos ingresados. Intente nuevamente.")

    # Opción 2: Buscar
    elif opcion == "2":
        rut_buscar = input("Ingrese el Rut a buscar: ").strip()
        if rut_buscar in afiliados:
            print("Información del afiliado:")
            print("Rut:", rut_buscar)
            for clave, valor in afiliados[rut_buscar].items():
                print(f"{clave}: {valor}")
        else:
            print("Rut no encontrado.")

    # Opción 3: Imprimir certificados
    elif opcion == "3":
        rut_certificado = input("Ingrese el Rut para imprimir certificados: ").strip()
        if rut_certificado in afiliados:
            monto = random.randint(1000, 1500)
            print("\n*** CERTIFICADO DE AFILIACIÓN ***")
            print(f"Monto del certificado: ${monto}")
            print("Datos del afiliado:")
            print("Rut:", rut_certificado)
            for clave, valor in afiliados[rut_certificado].items():
                print(f"{clave}: {valor}")
        else:
            print("Rut no encontrado. No se puede imprimir el certificado.")

    # Opción 4: Salir
    elif opcion == "4":
        print("\nGracias por usar el programa.")
        print("Desarrollado por: [Tu Nombre y Apellido] - Versión 1.0") break

    else:
        print("Opción no válida. Intente nuevamente.")

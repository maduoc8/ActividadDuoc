from random import randint
afiliado = 0
certificados = randint(1000, 1500)

cliente = {"rutes": [],
           "nombres": [],
           "apellidospaternos": [],
           "edades": [],
           "estadosciviles": [],
           "generos": [],
        "fechasdeafiliaciones": []}


while True:
    # Menu de opciones
    print("\n***** ISAPRE VIDA Y SALUD *****\n") 
    opcion = input(" \n1)Registrar afiliado\n2) Buscar afiliado\n3) Imprimir certificado\n4) Salir\n " \
    "Ingrese una opcion: ") 
    while True:
        if opcion == "1":
            rut = input("Ingrese su rut: ")
            cliente["rutes"].append(rut)
            nombre = input("Ingrese su nombre: ")
            cliente["nombres"].append(nombre)
            apellido_paterno = input("Ingrese su apellido paterno: ")
            cliente["apellidospaternos"].append(apellido_paterno)
            edad = int(input("Ingrese su edad: "))
            cliente["edades"].append(edad)
            estado_civil = str(input("Ingrese el estado civil: (c = casado), (s = soltero), (v = viudo)"))
            cliente["estadosciviles"].append(estado_civil)
            genero = input("Ingrese su genero: ")
            cliente["generos"].append(genero)
            fecha_de_afiliacion = input("Ingrese la fecha de afiliación: ")
            cliente["fechasdeafiliaciones"].append(fecha_de_afiliacion)            
            break
           
            
           
            
        
        if opcion == "2":
            if afiliado == 0:
                print("\nNO se han registrados afiliados !!\n")
            else:
                rut = input("\nIngresa RUT del afiliado")
            for rut in cliente.items():
                print(f"{cliente}")
                
      
        if opcion == "3":
            if afiliado == 0:
                print("\nNo se han registrado afiliados. ")
            else:
                rut_buscar = input("\nIngrese rut del afiliado para imprimir certificado: ") 
            if rut_buscar in cliente["rutes"]:
                indice = cliente["rutes"].index(rut_buscar)
                valor_certificado = random.randint(1000, 1500)
                print("\n=== CERTIFICADO DE AFILIACIÓN ===")
                print(f"Nombre del afiliado: {cliente['nombres'][indice]}")
                print(f"Apellido paterno: {cliente['apellidospaternos'][indice]}")
                print(f"RUT: {cliente['rutes'][indice]}")
                print(f"Edad: {cliente['edades'][indice]}")
                print(f"Estado civil: {cliente['estadosciviles'][indice]}")
                print(f"Género: {cliente['generos'][indice]}")
                print(f"Fecha de afiliación: {cliente['fechasdeafiliaciones'][indice]}")
                print(f"Valor del certificado: ${valor_certificado}")
                print("===============================\n")
            else:
                print("El RUT ingresado no existe en la base de datos.")       

        if opcion == "4":
            break
    break
   
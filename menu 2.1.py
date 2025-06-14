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



cliente={}
while True:
    # Menu de opciones
    print("\n***** ISAPRE VIDA Y SALUD *****\n") 
    opcion = input(" \n1)Registrar afiliado\n2) Buscar afiliado\n3) Imprimir certificado\n4) Salir\n " \
    "Ingrese una opcion: ") 
    while True:
        if opcion == '1':
            rut = input("Ingrese su rut: ")
            nombre = input("Ingrese su nombre: ")
            apellido_paterno = input("Ingrese su apellido paterno: ")
            edad = int(input("Ingrese su edad: "))
            estado_civil = str(input("Ingrese el estado civil: (c = casado), (s = soltero), (v = viudo)"))
            genero = input("Ingrese su genero: ")
            fecha_de_afiliacion = (input("Ingrese la fecha de afiliación: "))
            cliente["rutes"].append(rut)
            cliente["nombres"].append(nombre)
            cliente["apellidospaternos"].append(apellido_paterno)
            cliente["edades"].append(edad)
            cliente["estadosciviles"].append(estado_civil)
            cliente["generos"].append(genero)
            cliente["fechasdeafiliaciones"].append(fecha_de_afiliacion)
        
        if opcion == 2:
            if afiliado == 0:
                print("\nNO se han registrados afiliados !!\n")
            else:
                rut = input("\nIngresa RUT del afiliado")
            for rut in cliente.items():
                print(f"{cliente}")

        if opcion == 3:
            if certificados  == 0:
                print("\nNo se encontrado el rut. intente nuevamente")
            else:
                print()    


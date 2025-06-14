afiliado = 0
cliente = {"rutes": [],
           "nombres": [],
           "apellidospaternos": [],
           "edades": [],
           "estadosciviles": [],
           "generos": [],
        "fechasdeafiliaciones": []}

rut = input("Ingrese su rut: ")
nombre = input("Ingrese su nombre: ")
apellido_paterno = input("Ingrese su apellido paterno: ")
edad = int(input("Ingrese su edad: "))
estado_civil = str(input("Ingrese el estado civil: (c = casado), (s = soltero), (v = viudo)"))
genero = input("Ingrese su genero: ")
fecha_de_afiliacion = int(input("Ingrese la fecha de afiliación: "))

opcion = input("Ingrese una opcion (1 - 4): ")

if opcion == 1:
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
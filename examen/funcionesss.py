import numpy
listaruts=[]
creativos= numpy.zeros((10,10),int)
fecha="11/07/2023"
platinum=120000
gold= 80000
silver= 50000
acumulador_dinero = 0
contador_dinero = 0
total_entradas = 0
total_dinero = 0

lista_disponible=[]
def validar_nom():
    while True:
        nom =  input("Ingrese su nombre: ")
        if len(nom.strip()) >= 3:
            return nom
        else:
            print("ERROR! SU NOMBRE DEBE TENER 3 O MAS CARATCTERES!")

def validar_apellido():
    while True:
        apellido =  input("Ingrese su apellido: ")
        if len(apellido.strip()) >= 3:
            return apellido
        else:
            print("ERROR! SU NOMBRE DEBE TENER 3 O MAS CARATCTERES!")

def validar_rut():
    while True:
            try:
                rut = int(input("Ingrese su rut sin coma ni digito verificador: "))
                if len(str(rut))==8:
                    listaruts.append(rut)
                    return rut
                else:
                    print("ERROR! DEBE INGRESAR RUT SIN COMAS NI DIGITO VERIFICADOR!")
            except:
                print("ERROR! DEBE INGRESAR SU RUT CON NUMEROS ENTEROS!")

def validar_menu():
    while True:
        try:
            opc=int(input("Ingrese su opcion: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERROR! DEBE INGRESAR LA OPCION DEL 1 AL 5!")
        except:
            print("ERROR! DEBE INGRESARUN NUMERO ENTERO!")

def mostrar_menu():
    print("""Bienvenido a Creativos.cl, que desea realizar?
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")

def mostrar_cancha():
    for x in range(10):
        print(f"Fila {x+1}",end=" ")
        for y in range(10):
            print(creativos[x][y],end=" ")
            print()
            print()
            

def comprar_entrada():
    while True:
        try:
            entrada=int(input("Ingrese cuantas entradas desea(CON UN MAXIMO DE 3): "))
            if entrada >=1 and entrada <=3:
                
                return entrada
            else:
                print("ERROR! SOLO PUEDE COMPRAR UN MAXIMO DE 3 ENTRADAS!")
        except:
            print("ERROR! DEBE INGRESAR NUMEROS ENTEROS!")

def mostrar_lugar():
    while True:
        for x in range(10):
            for y in range(10):
             if creativos[x][y]==0:
                print("Lugar disponible")
             else:
                 print("Lugar ocupado")

def salir():
    print(f"Gracias por la visita {validar_nom}{validar_apellido}, Fecha:{fecha}")

def listado_asistentes():
    print(listaruts.sort)

def ganancias_totales():
    print(f"""
    _____________________________________________________________________
    |  Tipo entrada           / Cantidad          /        Total        |
    |-------------------------------------------------------------------|
    |  Platinum ${platinum}   /{contador_dinero}  /{acumulador_dinero}  |
    |-------------------------------------------------------------------|
    |  Gold ${gold}           /{contador_dinero}  /{acumulador_dinero}  |
    |-------------------------------------------------------------------|               
    |  Silver ${silver}       /{contador_dinero}  /{acumulador_dinero}  |
    |-------------------------------------------------------------------|
    |  Total                  /{total_entradas}   /{total_dinero}       |
    |___________________________________________________________________|
    """)

def val_fila():
    while True:
        try:
            fila = int(input("Ingrese en que fila se pisicionara(Del 1 al 10)): "))
            if fila in (1,2,3,4,5,6,7,8,9,10):
                if fila in (1,2,3):
                    acumulador_dinero = acumulador_dinero + platinum
                    return fila
                elif fila in (4,5,6):
                    acumulador_dinero = acumulador_dinero + gold
                    return fila
                elif fila in (7,8,9,10):
                    acumulador_dinero = acumulador_dinero + silver
                return fila
            else:
                print("ERROR! DEBE INGRESAR UNA FILA DEL 1 AL 1O!")
        except:
            print("ERROR! DEBE INGRESAR NUMEROS ENTEROS!")

def val_colum():
    while True:
        try:
            colum = int(input("Ingrese en que fila se pisicionara(Del 1 al 10)): "))
            if colum in (1,2,3,4,5,6,7,8,9,10):
                return colum
            else:
                print("ERROR! DEBE INGRESAR UNA COLUMNA DEL 1 AL 1O!")
        except:
            print("ERROR! DEBE INGRESAR NUMEROS ENTEROS!")

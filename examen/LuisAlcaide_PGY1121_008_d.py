import funcionesss as fn
import numpy
creativos = numpy.zeros((10,10),int)
listaruts=[]
print(fn.mostrar_menu())
opc = fn.validar_menu()
if opc ==1:
    comprarentrada=fn.comprar_entrada()
    cancha=fn.mostrar_cancha()
    rut=fn.validar_rut()
    nom=fn.validar_nom()
    ape=fn.validar_apellido()
    print("Su compra se ha realizo exitosamente!")
elif opc ==2:
    cancha=fn.mostrar_lugar
elif opc==3:
    asistentes=fn.listado_asistentes()
elif opc==4:
    total_dia=fn.ganancias_totales()
else:
    print(fn.salir())
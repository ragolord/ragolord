# prueba

import os
datos_libros=[]

def principal():
    while True:
        try:
            print("****PRESTAMOS DE LIBROS***")
            print("1.Registrar Libro")
            print("2.Prestar libro")
            print("3.Listar todos los libros")
            print("4.Imprimir reporte de préstamos")
            print("5. Salir del Programa")

            op=int(input("Ingresar una opcion de los libros:"))
        except ValueError:
            print("opcion invalida, ingrese un numero nuevamente")

        if op==1:
            registro_libro()

        elif op==2:
            prestar_libro()

        elif op==3:
            listar_libros()

        elif op==4:
            imprimir_reporte()
        
        elif op==5:
            print("Salir del programa")
            break
        else:
            print("Opcion invalida, ingrese un numero nuevamente")

def registro_libro():
        try:
            nombre_libro=input("Ingrese el nombre del libro:")
            autor=input("Ingrese el autor del libro:")
            ano_publicacion=int(input("Ingrese año de publicacion del libro:"))
            sku=input("ingrese el identificador sku de cada libro:")

            if nombre_libro=="" or autor=="" or ano_publicacion=="" or sku==autor or sku <= 0:
                print("Datos invalidos, ingrese los datos correctamente")
            

            datos_libro={'nombre_libro':nombre_libro,
                          'autor':autor,
                          'ano':ano_publicacion,
                          'sku':sku}
            datos_libros.append(datos_libro)
        except ValueError:
            print("todos los Datos estan ingrasados correctamente")

def prestar_libro():
    print("Prestar libros\t\tnombre_usuario\t\tsku\n")
    for dato_libro in datos_libros:
        print(dato_libro['nombre_libro'],"\t\t",dato_libro['autor'])






def listar_libros():
    print("Listar libros\t\tnombre_usuario\t\tsku\n")





def imprimir_reporte():
    try:
        op=int(input(""))

        if op==1:
            print("Reporte de libros prestados")



        elif op==2:
            print("Reporte de libros prestados")

        else:
            print("Opcion invalida, ingrese un numero nuevamente")
    except ValueError:
        print("Opcion invalida, ingrese un numero nuevamente")
            









        



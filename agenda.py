agenda=[(71554411,'sebastian','Castillo','Calero',922255445),(879879878,'johan','Isidro','Borja',465465465)]
while True:
    print("AGENDA")
    print("1. Agregar contactos")
    print("2. Listar Contactos")
    print("3. Buscador de Contacto")
    print("4. Salir")
    op=int(input("Ingrese opcion: "))
    print("")
    if op==1:
        cant=int(input("Cuantas personas quier ingresar: "))
        for i in range (cant):
            dni=int(input("DNI: "))  
            nombre=input("Nombre: ")
            apaterno=input("Apellido paterno: ")
            amaterno=input("Apellido materno: ")
            telefono=int(input("Telefono: "))
            print("")
            datos=(dni,nombre,apaterno,amaterno,telefono)
            agenda.append(datos)
    elif op==2:
        print("LISTAR AGENTA")
        for datos in (agenda):
            print("DNI: ",datos[0])
            print("Nombre completo:" ,datos[1]," ",datos[2]," ",datos[3])
            print("Telefono: ",datos[4],"\n")
    elif op==3:
        cont=0
        
        print("BUSCAR CONTACTO")
        nombre=input("Ingrese nombre: ")
        for datos in agenda:
            cont=cont+1
            if datos[1]==nombre:
                print("DNI: ",datos[0])
                print("Nombre completo:" ,datos[1]," ",datos[2]," ",datos[3])
                print("Telefono: ",datos[4],"\n")    
    elif op==4:
        break
    
        
        


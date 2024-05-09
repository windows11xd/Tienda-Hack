print("☠︎  ☠︎  ☠︎  𝕄 𝕁 ☠︎  ☠︎  ☠︎")

print("Ｒｅｇｉｓｔｒａｔｅ")

usuario = input("Ingrese Usuario: ")
contraseña = input("Ingrese Contraseña: ")

print("Procesando...")
print("\n")

print("✡︎✡︎✡︎ Servicios ✡︎✡︎✡︎")
print("""[1] Creación de virus        $ 100
[2] Creación de malware      $ 450
[3] Ataque a paginas         $ 600
[4] Ataque de scrips         $ 700
[5] Ataque DDos              $ 900
[6] ✝︎ ✝︎ ✝︎ ✝︎ ✝︎ ✝︎ Salir ✝︎ ✝︎ ✝︎ ✝︎ ✝︎ ✝︎""")
print("\n")
presupuesto = int(input("Ingrese su presupuesto o [6]: "))
if presupuesto >=7 and presupuesto <= 99:
    print("\n")
    print("No cuenta con el presupuesto necesario ☹")
    print("\n")
if presupuesto >= 100 and presupuesto <= 449:
    print("\n")
    print("""La opcion acorde a su presupuesto es: 
[1] Creación de virus        $ 100""")
    print("\n")
    op1 = int(input("Selecciona opción: "))
    if op1 == 1:
        print("Adquiriendo servicio de Creación de virus [$100] ")
        print("\n")
        print("Usuario:",usuario,"          Contraseña:",contraseña)
        confirmar = input("Confirmar pedido [ENTER]")
        print("\n")
        print("Cargando pedido...")
        print("Vuelto",presupuesto-100)
if presupuesto >= 450 and presupuesto <= 599:
    print("\n")
    print("""Las opciones acorde a su presupuesto son:
[1] Creación de virus        $ 100 
[2] Creación de malware      $ 450""")
    print("\n")
    op2 = int(input("Selecciona opción: "))
    match op2:
        case 1:
            print("Adquiriendo servicio de Creación de virus [$100] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-100)
        case 2:
            print("Adquiriendo servicio de Creación de malware [$450] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-450)
    
if presupuesto >= 600 and presupuesto <= 699:
    print("\n")
    print("""Las opciones acorde a su presupuesto son: 
[1] Creación de virus        $ 100
[2] Creación de malware      $ 450
[3] Ataque a paginas         $ 600""")
    print("\n")
    op3 = int(input("Selecciona opción: "))
    match op3:
        case 1:
            print("Adquiriendo servicio de Creación de virus [$100] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-100)
        case 2:
            print("Adquiriendo servicio de Creación de malware [$450] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-450)
        case 3:
            print("Adquiriendo servicio de Ataque a Paginas [$600] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-600)
    
if presupuesto >= 700 and presupuesto <= 899:
    print("\n")
    print("""Las opciones acorde a su presupuesto son: 
[1] Creación de virus        $ 100
[2] Creación de malware      $ 450
[3] Ataque a paginas         $ 600
[4] Ataque de scrips         $ 700""")
    print("\n")
    op4 = int(input("Selecciona opción: "))
    match op4:
        case 1:
            print("Adquiriendo servicio de Creación de virus [$100] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-100)
        case 2:
            print("Adquiriendo servicio de Creación de malware [$450] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-450)
        case 3:
            print("Adquiriendo servicio de Ataque a Paginas [$600] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-600)
        case 4:
            print("Adquiriendo servicio de Ataque de scrips [$700] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-700)
    
if presupuesto >= 900:
    print("\n")
    print("""Las opciones acorde a su presupuesto son: 
[1] Creación de virus        $ 100
[2] Creación de malware      $ 450
[3] Ataque a paginas         $ 600
[4] Ataque de scrips         $ 700
[5] Ataque DDos              $ 900""")
    print("\n")
    op5 = int(input("Selecciona opción: "))
    match op5:
        case 1:
            print("Adquiriendo servicio de Creación de virus [$100] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-100)
        case 2:
            print("Adquiriendo servicio de Creación de malware [$450] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-450)
        case 3:
            print("Adquiriendo servicio de Ataque a Paginas [$600] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-600)
        case 4:
            print("Adquiriendo servicio de Ataque de scrips [$700] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-700)
        case 5:
            print("Adquiriendo servicio de Ataque DDos [$900] ")
            print("\n")
            print("Usuario:",usuario,"          Contraseña:",contraseña)
            confirmar = input("Confirmar pedido [ENTER]")
            print("\n")
            print("Cargando pedido...")
            print("Vuelto",presupuesto-900)

if presupuesto == 6:
    print("Gracias por tu visita",usuario)
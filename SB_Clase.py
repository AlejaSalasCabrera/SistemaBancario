#Alejandra_salas

data = []

# ****************************************************************
class Cuota:
    val_cuota = 0
    id_prestamo = 0
    estado = False

    def __init__(self,val_cuota, id_prestamo,estado):
        self.val_cuota = val_cuota
        self.id_prestamo = id_prestamo
        self.estado = estado

    def crear_cuota(self, pos, numc):

        ct = {
            'val_cuota': self.val_cuota,
            'id_prestamo' : self.id_prestamo,
            'estado': self.estado
        }
        listtmp = list(data[pos]['cuotas'])

        for c in range(1, (numc+1)):
            listtmp.append(ct)
        data[pos]['cuotas'] = listtmp

# ****************************************************************
class Prestamo:
    valor = 0
    num_cuotas = 0


    def __init__(self, valor, num_cuotas):
        self.valor = valor
        self.num_cuotas = num_cuotas

    def crear_prestamo(self, pos):
        p = {
            'valor': self.valor,
            'num_cuotas': self.num_cuotas
        }

        listatmp = list(data[pos]['prestamos'])
        listatmp.append(p)
        data[pos]['prestamos'] = listatmp

        poslist = len(listatmp)-1

        val = int(self.valor) / int(self.num_cuotas)

        cuota = Cuota(val, int(poslist), False)
        cuota.crear_cuota(pos, int(self.num_cuotas))


# ****************************************************************

class Usuario(Prestamo, Cuota):
    identificacion = ""
    nombre = ""
    telefono = ""
    correo =\
        ""
    def __init__(self, identificacion, nombre, telefono, correo, valor, num_cuotas,val_cuota, id_prestamo,estado):
        Prestamo.__init__(self, valor, num_cuotas)
        Cuota.__init__(self,val_cuota, id_prestamo,estado)
        self.identificacion = identificacion
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo


    def crear_usuario(self):
        u = {
        'identificacion': self.identificacion,
        'nombre': self.nombre,
        'telefono': self.telefono,
        'correo': self.correo
        }

        data.append({'usuarios' : [u],'prestamos' : [], 'cuotas':[]})

# ****************************************************************

def pagar_cuota(pos):
    print("")
    posp = 0
    for p in list(data[pos]['prestamo']):
        print("(ID : {}) El Valor del prestamo es: {}".format(posp, p['valor']))
        posp = posp + 1

    idp = input("Digite el ide del prestamo que desea realizar el pago: ")


    listtmp =data[pos]['cuota']
    for c in listtmp:
        if c['id_prestamo'] == int(idp):
            c['estado']= True
        break


    data[pos]['cuota']=listtmp
    print(data)
    print('')
    menu()

def crear_prestamo(pos):
    val = input("Digite el valor del prestamo: ")
    numc = input("Digite el numero de cuotas del prestamo: ")

    prestamo = Prestamo(int(val), int(numc))
    prestamo.crear_prestamo(pos)

    print(data)
    print('')
    menu()

def buscar_usuario(opt):
    usu = input("Digite la cedula de usuario: ")
    for u in data:
        pos = 0
        if u['usuarios'][0]['identificacion'] == usu:
            if opt ==2:
                crear_prestamo(pos)
            elif opt ==3:
                pagar_cuota(pos)
        break
        pos = pos + 1


def crear_usuario():
    ident = input('Digite la identificacion:')
    nom = input('Digite el nombre:')
    tel = input('Digite telefono: ')
    correo = input('Digite correo: ')
    print('')
    usuario = Usuario(ident, nom, tel, correo, 0, 0, 0, 0, False)
    usuario.crear_usuario()

    print(data)
    print('')
    menu()

def procesar_opciones(opc):
    if opc == 1:
        crear_usuario()
    elif opc == 2:
        buscar_usuario(2)
    elif opc == 3:
        buscar_usuario(3)
    elif opc == 4:
        crear_usuario()


def menu():
    print("*** MI BANCO ***")
    print("(1). Registrar usuarios")
    print("(2). Realizar prestamos")
    print("(3). Pagos de cuotas")
    print("(1). Reportes")
    print("")
    opcion = int(input("seleccionar opcion:"))

    procesar_opciones(opcion)

menu()
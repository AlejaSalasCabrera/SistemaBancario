#ALejandra Salas

user = []
pres = []
cuo = []

class Prestamo:
    id_userp = 0
    cant_pres = 0
    num_cuo_pres = 0

    def Registrar_prestamo(self):
        self.id_userp = input("digite la id de usuario: ")
        for iu in user:
            if iu['id'] == self.id_userp:
                self.cant_pres = int(input("Ingrese la cantidad del prestamo "))
                self.num_cuo_pres = int(input("Ingrese numero de cuotas del prestamo "))
                pres.append({'id_user': self.id_userp,'can_pres': self.cant_pres, 'num_cuo': self.num_cuo_pres})
                nc = self.num_cuo_pres
                if (nc > 0):
                    c = 0
                    valor_cuota = self.cant_pres/self.num_cuo_pres
                    while c != nc:
                        cuo.append({'id_user': self.id_userp, 'valor_pres': valor_cuota, 'estado':False})
                        c = c + 1

class Cuota:
    valor_cuo = 0

    #def Pagar_cuota(self):




class User(Prestamo):
    Id_user = 0
    nom_user = ""

    def Registro_User(self):
        self.Id_user = input("Ingrese su identificacion: ")
        self.nom_user = input("Digite su nombre: ")
        user.append({'id': self.Id_user, 'nom': self.nom_user})



print("MENU DE OPCIONES")
print("1. Crear Usuario")
print("2. Solicitar Prestamo")
print("3. Pagar cuotas")
print("4. Reportes")
print("\n")
opc =int(input("Digite la opcion: "))


while opc != 5:
    usuario = User()

    if opc == 1:
        usuario.Registro_User()
        print(user)

    elif opc == 2:
        usuario.Registrar_prestamo()
        print(pres)
        print(cuo)

    elif opc == 3:
        print("3")

    elif opc == 4:
        print("1. Consultar numero de cuotas pagadas")
        print("2. Consultar numero de cuotas en mora")
        print("3. Consultar todos sus prestamos")

        nopc = int(input("Digite la opcion para de reportes que desea optener: "))
        while nopc != 4:

            if nopc == 1:
                print("1,1")

            elif nopc == 2:
                print("1,2")

            elif nopc == 3:
                print("1,3")

            else:
                print('La opcion digitada no existe')

            nopc = int(input("\nDigite la opcion Nuevamente: "))

    else:
        print('La opcion digitada no existe')

    opc =int(input("\nDigite la opcion: "))
